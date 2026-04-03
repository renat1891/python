import asyncio
import os
import re
from io import BytesIO

from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
)

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

API_TOKEN = "8696285101:AAGWb3IpA9i9Fp7dSSZxvrY4ARMn_Yf2tyM"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class ResumeForm(StatesGroup):
    full_name   = State()
    job_title   = State()
    phone       = State()
    email       = State()
    city        = State()
    about       = State()
    experience  = State()
    education   = State()
    skills      = State()
    languages   = State()


STEPS = [
    ("full_name",  "Введіть своє повне ім'я:\n\nПриклад: Іваненко Олег Петрович"),
    ("job_title",  "Бажана посада:\n\nПриклад: Frontend Developer"),
    ("phone",      "Номер телефону:\n\nПриклад: +380991234567"),
    ("email",      "Email адреса:\n\nПриклад: ivan@gmail.com"),
    ("city",       "Місто проживання:\n\nПриклад: Київ"),
    ("about",      "Коротко про себе (2–4 речення):\n\nПриклад: Відповідальний розробник з 3 роками досвіду..."),
    ("experience", "Досвід роботи:\n\nФормат (кожне місце з нового рядка):\nКомпанія | Посада | Рік–Рік\n\nПриклад:\nSoftServe | Junior Dev | 2022–2023\nEpam | Middle Dev | 2023–досі"),
    ("education",  "Освіта:\n\nПриклад: КПІ, Комп'ютерні науки, 2018–2022"),
    ("skills",     "Навички (через кому):\n\nПриклад: Python, Django, PostgreSQL, Docker, Git"),
    ("languages",  "Мови (через кому):\n\nПриклад: Українська (рідна), Англійська (B2), Польська (A2)"),
]

STEP_KEYS = [s[0] for s in STEPS]


def skip_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⏭ Пропустити")]],
        resize_keyboard=True
    )


ACCENT = colors.HexColor("#1a237e")  
LIGHT  = colors.HexColor("#e8eaf6")   
GRAY   = colors.HexColor("#546e7a")


def build_resume_pdf(data: dict) -> BytesIO:
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=15*mm, bottomMargin=15*mm
    )

    styles = getSampleStyleSheet()

    
    name_style = ParagraphStyle("Name",
        fontSize=24, leading=28, textColor=ACCENT,
        fontName="Helvetica-Bold", alignment=TA_CENTER)

    title_style = ParagraphStyle("Title",
        fontSize=13, leading=16, textColor=GRAY,
        fontName="Helvetica", alignment=TA_CENTER)

    contact_style = ParagraphStyle("Contact",
        fontSize=9, leading=13, textColor=GRAY,
        fontName="Helvetica", alignment=TA_CENTER)

    section_style = ParagraphStyle("Section",
        fontSize=11, leading=14, textColor=colors.white,
        fontName="Helvetica-Bold", alignment=TA_LEFT,
        leftIndent=4)

    body_style = ParagraphStyle("Body",
        fontSize=10, leading=14, textColor=colors.HexColor("#212121"),
        fontName="Helvetica")

    job_style = ParagraphStyle("Job",
        fontSize=10, leading=13, textColor=ACCENT,
        fontName="Helvetica-Bold")

    meta_style = ParagraphStyle("Meta",
        fontSize=9, leading=12, textColor=GRAY,
        fontName="Helvetica-Oblique")

    story = []

    def section_header(text):
        tbl = Table([[Paragraph(f"  {text}", section_style)]], colWidths=[174*mm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), ACCENT),
            ("ROWBACKGROUNDS", (0,0), (-1,-1), [ACCENT]),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("ROUNDEDCORNERS", [3,3,3,3]),
        ]))
        story.append(Spacer(1, 6))
        story.append(tbl)
        story.append(Spacer(1, 6))

    story.append(Paragraph(data.get("full_name", ""), name_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph(data.get("job_title", ""), title_style))
    story.append(Spacer(1, 5))

    contacts = []
    if data.get("phone"):   contacts.append(f" {data['phone']}")
    if data.get("email"):   contacts.append(f" {data['email']}")
    if data.get("city"):    contacts.append(f" {data['city']}")
    story.append(Paragraph("   |   ".join(contacts), contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT))

    
    if data.get("about"):
        section_header("ПРО СЕБЕ")
        story.append(Paragraph(data["about"], body_style))

    
    if data.get("experience"):
        section_header("ДОСВІД РОБОТИ")
        for line in data["experience"].strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                story.append(Paragraph(f"{parts[1]} — {parts[0]}", job_style))
                story.append(Paragraph(parts[2], meta_style))
            else:
                story.append(Paragraph(line, body_style))
            story.append(Spacer(1, 5))

    
    if data.get("education"):
        section_header("ОСВІТА")
        story.append(Paragraph(data["education"], body_style))


    if data.get("skills"):
        section_header("НАВИЧКИ")
        skill_list = [s.strip() for s in data["skills"].split(",") if s.strip()]
        cols = 3
        rows = [skill_list[i:i+cols] for i in range(0, len(skill_list), cols)]
        while rows and len(rows[-1]) < cols:
            rows[-1].append("")
        cell_style = ParagraphStyle("Cell",
            fontSize=9, fontName="Helvetica",
            textColor=ACCENT)
        table_data = [[Paragraph(f"▸ {c}", cell_style) for c in row] for row in rows]
        tbl = Table(table_data, colWidths=[58*mm]*cols)
        tbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), LIGHT),
            ("ROWBACKGROUNDS", (0,0), (-1,-1), [LIGHT, colors.white]),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#c5cae9")),
        ]))
        story.append(tbl)

    if data.get("languages"):
        section_header("МОВИ")
        story.append(Paragraph(data["languages"], body_style))

    doc.build(story)
    buf.seek(0)
    return buf

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Вітаю! Я допоможу створити твоє резюме у форматі PDF.\n\n"
        "Заповни просту форму — і отримаєш готовий документ!\n\n"
        "Натисни /new щоб почати.",
        reply_markup=ReplyKeyboardRemove()
    )

@dp.message(F.text == "/new")
async def cmd_new(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(ResumeForm.full_name)
    await message.answer(
        STEPS[0][1],
        reply_markup=ReplyKeyboardRemove()
    )

async def next_step(message: types.Message, state: FSMContext, current_key: str, value: str):
    """Зберігає значення і переходить до наступного кроку"""
    if value != "Пропустити":
        await state.update_data({current_key: value})
    else:
        await state.update_data({current_key: ""})

    idx = STEP_KEYS.index(current_key)
    next_idx = idx + 1

    if next_idx < len(STEPS):
        next_key, next_prompt = STEPS[next_idx]
        next_state = getattr(ResumeForm, next_key)
        await state.set_state(next_state)

        # Показуємо прогрес
        progress = f"[{next_idx + 1}/{len(STEPS)}] "
        kb = skip_keyboard() if next_idx > 4 else ReplyKeyboardRemove()
        await message.answer(progress + next_prompt, reply_markup=kb)
    else:
        await generate_pdf(message, state)



@dp.message(ResumeForm.full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    await next_step(message, state, "full_name", message.text)

@dp.message(ResumeForm.job_title)
async def process_job_title(message: types.Message, state: FSMContext):
    await next_step(message, state, "job_title", message.text)

@dp.message(ResumeForm.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await next_step(message, state, "phone", message.text)

@dp.message(ResumeForm.email)
async def process_email(message: types.Message, state: FSMContext):
    await next_step(message, state, "email", message.text)

@dp.message(ResumeForm.city)
async def process_city(message: types.Message, state: FSMContext):
    await next_step(message, state, "city", message.text)

@dp.message(ResumeForm.about)
async def process_about(message: types.Message, state: FSMContext):
    await next_step(message, state, "about", message.text)

@dp.message(ResumeForm.experience)
async def process_experience(message: types.Message, state: FSMContext):
    await next_step(message, state, "experience", message.text)

@dp.message(ResumeForm.education)
async def process_education(message: types.Message, state: FSMContext):
    await next_step(message, state, "education", message.text)

@dp.message(ResumeForm.skills)
async def process_skills(message: types.Message, state: FSMContext):
    await next_step(message, state, "skills", message.text)

@dp.message(ResumeForm.languages)
async def process_languages(message: types.Message, state: FSMContext):
    await next_step(message, state, "languages", message.text)


async def generate_pdf(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()

    await message.answer("Генерую твоє резюме...", reply_markup=ReplyKeyboardRemove())

    try:
        pdf_buf = build_resume_pdf(data)
        name = data.get("full_name", "resume").replace(" ", "_")
        filename = f"resume_{name}.pdf"

        await message.answer_document(
            document=types.BufferedInputFile(pdf_buf.read(), filename=filename),
            caption=(
                f"Резюме готове!\n\n"
                f"{data.get('full_name', '')}\n"
                f"{data.get('job_title', '')}\n\n"
                "Щоб створити нове — натисни /new"
            )
        )
    except Exception as e:
        await message.answer(f"Помилка при генерації PDF: {e}\n\nСпробуй /new знову")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())