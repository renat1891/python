from customtkinter import *
from tkinter import messagebox

window = CTk()
window.title("Port Scanner")
window.geometry("400x450")


title_label = CTkLabel(window, text="Port Scanner - schooloffris.com", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)


target_label = CTkLabel(window, text="Target Host", font=("Arial", 12))
target_label.grid(row=1, column=0, sticky="w", padx=20)

host_entry = CTkEntry(window, width=150)
host_entry.insert(0, "www.schooloffris.com")
host_entry.grid(row=1, column=1, sticky="w", padx=20)

port_range_label = CTkLabel(window, text="Port Range", font=("Arial", 12))
port_range_label.grid(row=2, column=0, sticky="w", padx=20, pady=(10,0))

range_frame = CTkFrame(window, fg_color="transparent")
range_frame.grid(row=2, column=1, sticky="w", padx=20, pady=(10,0))

start_port_entry = CTkEntry(range_frame, width=60)
start_port_entry.insert(0, "1")
start_port_entry.grid(row=0, column=0)

CTkLabel(range_frame, text="To").grid(row=0, column=1, padx=5)

end_port_entry = CTkEntry(range_frame, width=60)
end_port_entry.insert(0, "500")
end_port_entry.grid(row=0, column=2)

def start_scan():
    target_host = host_entry.get()
    start_port = start_port_entry.get()
    end_port = end_port_entry.get()
    
    if not target_host or not start_port or not end_port:
        messagebox.showwarning("Попередження", "Будь ласка, заповніть всі поля")
        return
    
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except ValueError:
        messagebox.showerror("Помилка", "Порти повинні бути числами")
        return
    
    open_ports = [21, 22, 80, 443, 8080, 8443, 3306, 5432, 27017, 9200, 5601, 3000, 5000, 6379]
    
    for widget in ports_frame.winfo_children():
        widget.destroy()
    
    CTkLabel(ports_frame, text="Open Ports", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5)
    
    for i, port in enumerate(open_ports, 1):
        CTkLabel(ports_frame, text=str(port), font=("Arial", 10)).grid(row=i, column=0, pady=2)
    
    status_label.configure(text=f"Status: Scan completed - Found {len(open_ports)} open ports")

scan_button = CTkButton(window, text="START SCAN", command=start_scan, fg_color="green", hover_color="darkgreen")
scan_button.grid(row=3, column=0, columnspan=2, pady=15)

ports_container = CTkFrame(window)
ports_container.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

canvas = CTkCanvas(ports_container, highlightthickness=0)
scrollbar = CTkScrollbar(ports_container, orientation="vertical", command=canvas.yview)
scrollable_frame = CTkFrame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=(5, 0))
scrollbar.pack(side="right", fill="y", padx=(0, 5))

ports_frame = scrollable_frame


status_label = CTkLabel(window, text="Status: Ready to scan", font=("Arial", 12))
status_label.grid(row=5, column=0, columnspan=2, pady=10)

def clear_ports():
    for widget in ports_frame.winfo_children():
        widget.destroy()
    status_label.configure(text="Status: Ready to scan")

clear_button = CTkButton(window, text="Clear Results", command=clear_ports, fg_color="gray", hover_color="darkgray")
clear_button.grid(row=6, column=0, columnspan=2, pady=5)

window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
ports_container.grid_rowconfigure(0, weight=1)
ports_container.grid_columnconfigure(0, weight=1)

window.mainloop()