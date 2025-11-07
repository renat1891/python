

from customtkinter import *
from tkinter import messagebox
import socket
import threading
from queue import Queue, Empty


set_appearance_mode("System")
set_default_color_theme("blue")

app = CTk()
app.title("Simple Port Scanner")
app.geometry("420x520")

CTkLabel(app, text="Simple Port Scanner", font=("Arial", 16, "bold")).pack(pady=10)

CTkLabel(app, text="Target (host / domain):").pack(anchor="w", padx=20)
target_entry = CTkEntry(app, width=300)
target_entry.insert(0, "example.com")
target_entry.pack(padx=20, pady=5)

CTkLabel(app, text="Port range (e.g. 1 to 100):").pack(anchor="w", padx=20)
range_frame = CTkFrame(app, fg_color="transparent")
range_frame.pack(pady=5)

start_port = CTkEntry(range_frame, width=80)
start_port.insert(0, "1")
start_port.pack(side="left", padx=5)

CTkLabel(range_frame, text="to").pack(side="left")

end_port = CTkEntry(range_frame, width=80)
end_port.insert(0, "100")
end_port.pack(side="left", padx=5)

CTkLabel(app, text="").pack() 

CTkLabel(app, text="Results:").pack(anchor="w", padx=20)
result_box = CTkTextbox(app, width=360, height=300)
result_box.pack(padx=20, pady=5)
result_box.configure(state="disabled")

status_label = CTkLabel(app, text="Status: Idle", font=("Arial", 12))
status_label.pack(pady=6)

def clear_results():
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.configure(state="disabled")
    status_label.configure(text="Status: Idle")

CTkButton(app, text="Start Scan", fg_color="green", hover_color="darkgreen", command=lambda: start_scan()).pack(pady=(6,3))
CTkButton(app, text="Clear", fg_color="gray", hover_color="darkgray", command=clear_results).pack()

ui_queue = Queue()

def scan_port(host_ip, port, timeout=0.8):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        res = s.connect_ex((host_ip, port))
        s.close()
        return res == 0
    except Exception:
        return False

def worker_scan(host, start_p, end_p):
    try:
        ip = socket.gethostbyname(host)
    except Exception as e:
        ui_queue.put(("error", f"{host} — DNS error: {e}"))
        ui_queue.put(("done", 0))
        return

    ui_queue.put(("info", f"Scanning {host} ({ip}) ports {start_p}-{end_p}"))
    open_count = 0
    total = end_p - start_p + 1
    scanned = 0

    for p in range(start_p, end_p + 1):
        is_open = scan_port(ip, p)
        scanned += 1
        if is_open:
            open_count += 1
            ui_queue.put(("open", p))
        else:
            ui_queue.put(("closed", p))
        if scanned % 5 == 0 or scanned == total:
            ui_queue.put(("progress", scanned, total))  
    ui_queue.put(("done", open_count))

def process_queue():
    try:
        while True:
            item = ui_queue.get_nowait()
            tag = item[0]
            if tag == "info":
                text = item[1]
                result_box.configure(state="normal")
                result_box.insert("end", text + "\n")
                result_box.configure(state="disabled")
            elif tag == "error":
                text = item[1]
                result_box.configure(state="normal")
                result_box.insert("end", "ERROR: " + text + "\n")
                result_box.configure(state="disabled")
                status_label.configure(text="Status: Error")
            elif tag == "open":
                port = item[1]
                result_box.configure(state="normal")
                result_box.insert("end", f"Port {port} — OPEN\n")
                result_box.configure(state="disabled")
            elif tag == "closed":
                port = item[1]
                result_box.configure(state="normal")
                result_box.insert("end", f"Port {port} — closed\n")
                result_box.configure(state="disabled")
            elif tag == "progress":
                scanned, total = item[1], item[2]
                status_label.configure(text=f"Status: Scanning... {scanned}/{total}")
            elif tag == "done":
                open_count = item[1]
                status_label.configure(text=f"Status: Done — {open_count} open ports")
                result_box.configure(state="normal")
                result_box.insert("end", f"\nScan finished — {open_count} open ports found.\n")
                result_box.configure(state="disabled")
    except Empty:
        pass
    app.after(150, process_queue)

app.after(150, process_queue)

def start_scan():
    host = target_entry.get().strip()
    if not host:
        messagebox.showwarning("Warning", "Please enter target host")
        return
    try:
        s_port = int(start_port.get().strip())
        e_port = int(end_port.get().strip())
        if s_port < 1 or e_port > 65535 or s_port > e_port:
            raise ValueError
    except Exception:
        messagebox.showerror("Error", "Please enter valid port numbers (1-65535)")
        return

    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.configure(state="disabled")
    status_label.configure(text="Status: Preparing...")
    t = threading.Thread(target=worker_scan, args=(host, s_port, e_port), daemon=True)
    t.start()

app.mainloop()

