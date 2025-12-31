import tkinter as tk
from tkinter import ttk

def clear_screen():
    """Removes all widgets from the root window."""
    for widget in root.winfo_children():
        widget.destroy()

# --- Placeholder Logic Helpers ---
def on_entry_click(event, default_text):
    if event.widget.get() == default_text:
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')

def on_focusout(event, default_text):
    if event.widget.get() == '':
        event.widget.insert(0, default_text)
        event.widget.config(fg='grey')

# --- POPUP: LOCATION SELECTION (Overlay on Home Page) ---
def show_location_selection(entry_to_update):
    """Shows the location selection as a centered popup overlay."""
    loc_pop = tk.Toplevel(root)
    loc_pop.overrideredirect(True)
    
    # Matching the size and position to look like an overlay
    width, height = 360, 600
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    loc_pop.geometry(f"{width}x{height}+{x}+{y}")
    loc_pop.configure(bg="white", highlightbackground="#ddd", highlightthickness=1)
    
    # Close Button (X icon)
    close_frame = tk.Frame(loc_pop, bg="white")
    close_frame.pack(fill="x", pady=10)
    tk.Button(close_frame, text="✕", font=("Arial", 16, "bold"), bg="black", fg="white", 
              bd=0, command=loc_pop.destroy, width=2, cursor="hand2").pack()

    # Search Bar (Matches Image 3)
    search_frame = tk.Frame(loc_pop, bg="white", highlightthickness=1, highlightbackground="#eee")
    search_frame.pack(fill="x", padx=20, pady=10)
    tk.Label(search_frame, text="🔍", bg="white", fg="grey").pack(side="left", padx=5)
    tk.Entry(search_frame, font=("Arial", 11), bd=0).pack(side="left", fill="x", expand=True, pady=10)

    # Use My Location Button
    tk.Button(loc_pop, text="🎯 Use My Location", font=("Arial", 10, "bold"), 
              fg="#e91e63", bg="white", relief="groove", bd=1, pady=8).pack(fill="x", padx=20, pady=10)

    tk.Label(loc_pop, text="Popular Areas", font=("Arial", 12, "bold"), bg="white", fg="#555").pack(anchor="w", padx=20, pady=5)

    # Grid for Locations
    grid_container = tk.Frame(loc_pop, bg="white")
    grid_container.pack(fill="both", expand=True, padx=10)

    locations = [
        "Thudiyalur", "Saravanampatti", "Narasimhanaicken Palayam",
        "Periyanaickenpalayam", "Veerapandi", "Kalapatti", "Martins"
    ]

    row, col = 0, 0
    for loc in locations:
        btn = tk.Button(grid_container, text=loc, font=("Arial", 8, "bold"), bg="white", fg="#2f2f4f",
                        relief="ridge", width=14, height=4, wraplength=90,
                        command=lambda l=loc: [entry_to_update.delete(0, tk.END), 
                                               entry_to_update.insert(0, l), 
                                               entry_to_update.config(fg='black'),
                                               loc_pop.destroy()])
        btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
        col += 1
        if col > 2: col = 0; row += 1

# --- POPUP: FILTER ---
def show_filter_popup():
    filter_pop = tk.Toplevel(root)
    filter_pop.title("Filter")
    width, height = 380, 680
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    filter_pop.geometry(f"{width}x{height}+{x}+{y}")
    filter_pop.configure(bg="#f8f9fb")

    header = tk.Frame(filter_pop, bg="white", pady=10)
    header.pack(fill="x")
    tk.Button(header, text="←", font=("Arial", 16), bd=0, bg="white", command=filter_pop.destroy).pack(side="left", padx=10)
    tk.Label(header, text="Filter", font=("Arial", 14, "bold"), bg="white").pack(side="left", padx=10)
    tk.Button(header, text="Clear", fg="#e91e63", font=("Arial", 10, "bold"), bd=1, relief="solid", bg="white", padx=10).pack(side="right", padx=10)

    search_bg = tk.Frame(filter_pop, bg="#32344a", padx=20, pady=25)
    search_bg.pack(fill="x", padx=15, pady=15)
    
    tk.Entry(search_bg, font=("Arial", 11), bg="#32344a", fg="white", insertbackground="white", bd=0).pack(fill="x")
    tk.Label(search_bg, text="Type company eg. Blinkit", fg="#aaa", bg="#32344a", font=("Arial", 9)).place(x=20, y=25)
    tk.Frame(search_bg, height=1, bg="#777").pack(fill="x", pady=(5, 15))

    tk.Entry(search_bg, font=("Arial", 11), bg="#32344a", fg="white", insertbackground="white", bd=0).pack(fill="x")
    tk.Label(search_bg, text="Location", fg="#aaa", bg="#32344a", font=("Arial", 9)).place(x=20, y=75)
    tk.Frame(search_bg, height=1, bg="#777").pack(fill="x", pady=5)

    def create_section(parent, title, options):
        tk.Label(parent, text=title, font=("Arial", 11, "bold"), bg="#f8f9fb", fg="#333").pack(anchor="w", padx=20, pady=(15, 5))
        frame = tk.Frame(parent, bg="#f8f9fb")
        frame.pack(fill="x", padx=15)
        for i, opt in enumerate(options):
            btn = tk.Button(frame, text=opt, font=("Arial", 9), bg="white", fg="#333", relief="flat", 
                            highlightbackground="#ddd", highlightthickness=1, padx=10, pady=5)
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
        for i in range(2): frame.columnconfigure(i, weight=1)

    create_section(filter_pop, "Work Type", ["FullTime-Permanent", "FullTime-Contract", "PartTime-Permanent", "PartTime-Contract"])
    
    tk.Label(filter_pop, text="Work Policy", font=("Arial", 11, "bold"), bg="#f8f9fb", fg="#333").pack(anchor="w", padx=20, pady=(15, 5))
    policy_frame = tk.Frame(filter_pop, bg="#f8f9fb")
    policy_frame.pack(fill="x", padx=15)
    for opt in ["On Site", "Work From Home", "Hybrid"]:
        tk.Button(policy_frame, text=opt, font=("Arial", 9), bg="white", fg="#333", relief="flat", 
                  highlightbackground="#ddd", highlightthickness=1, padx=8, pady=5).pack(side="left", padx=5)

    create_section(filter_pop, "Experience Required", ["Fresher", "Experience"])

    tk.Button(filter_pop, text="Submit", bg="#e91e63", fg="white", font=("Arial", 14, "bold"), 
              bd=0, pady=10, command=filter_pop.destroy).pack(fill="x", padx=20, side="bottom", pady=20)

# --- POPUP: SORT ---
def show_sort_popup():
    sort_pop = tk.Toplevel(root)
    sort_pop.overrideredirect(True)
    width, height = 320, 350
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    sort_pop.geometry(f"{width}x{height}+{x}+{y}")
    
    main_frame = tk.Frame(sort_pop, bg="white", highlightbackground="#ddd", highlightthickness=1)
    main_frame.pack(fill="both", expand=True)
    tk.Label(main_frame, text="Sort", font=("Arial", 18, "bold"), fg="#e91e63", bg="white", pady=20).pack()
    tk.Frame(main_frame, height=1, bg="#eee").pack(fill="x", padx=10)

    options = ["Most Recent", "Salary(max-min)", "Salary(min-max)", "Distance(Near To Far)"]
    for opt in options:
        btn = tk.Button(main_frame, text=opt, font=("Arial", 12), bg="white", fg="#333", 
                        activebackground="#f5f5f5", bd=0, pady=12, 
                        command=lambda o=opt: [print(f"Sorting by: {o}"), sort_pop.destroy()])
        btn.pack(fill="x")
        tk.Frame(main_frame, height=1, bg="#f0f0f0").pack(fill="x", padx=25)

    tk.Button(main_frame, text="Cancel", font=("Arial", 11, "bold"), fg="#333", bg="white", 
              relief="ridge", width=12, pady=5, command=sort_pop.destroy).pack(pady=20)

# --- PAGE: JOBS LISTING ---
def show_jobs_page(filter_category=None):
    clear_screen()
    root.configure(bg="#f8f9fb")

    top_bar = tk.Frame(root, bg="white", pady=10)
    top_bar.pack(fill="x")
    
    header_text = f"🔍 {filter_category}" if filter_category else "🔍 Search..."
    tk.Label(top_bar, text=header_text, fg="grey", bg="white", font=("Arial", 11)).pack(side="left", padx=15)
    
    sort_lbl = tk.Label(top_bar, text="↕ Sort", fg="black", bg="white", font=("Arial", 11), cursor="hand2")
    sort_lbl.pack(side="left", padx=20)
    sort_lbl.bind("<Button-1>", lambda e: show_sort_popup())
    
    filter_lbl = tk.Label(top_bar, text="≡ Filter", fg="black", bg="white", font=("Arial", 11), cursor="hand2")
    filter_lbl.pack(side="left", padx=20)
    filter_lbl.bind("<Button-1>", lambda e: show_filter_popup())

    banner = tk.Frame(root, bg="#f5f5f5", pady=8)
    banner.pack(fill="x", padx=15, pady=10)
    tk.Label(banner, text="🚫 If someone asks for money for job Say No and Report 🚩", 
             font=("Arial", 8, "bold"), bg="#f5f5f5").pack()

    container = tk.Frame(root, bg="#f8f9fb")
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg="#f8f9fb", highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f8f9fb")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_frame, width=e.width))

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    job_listings = [
        {"title": "Usha Electricals", "salary": "₹ 8000 - 12000", "exp": "1-5 Year(s)", "cat": "Electrician"},
        {"title": "Sri Kannimar Enterprises", "salary": "₹ 5000 - 10000", "exp": "1-5 Year(s)", "cat": "Plumber"},
        {"title": "Om Sakthi Welders", "salary": "₹ 12000 - 15000", "exp": "0-2 Year(s)", "cat": "Welders"},
        {"title": "Ganesh Carpentry Shop", "salary": "₹ 6000 - 9000", "exp": "1-4 Year(s)", "cat": "Carpenter"},
        {"title": "City Warehouse Hub", "salary": "₹ 8000 - 11000", "exp": "1-2 Year(s)", "cat": "Warehouse"},
        {"title": "Urban Painter Services", "salary": "₹ 9000 - 13000", "exp": "3-7 Year(s)", "cat": "Painter"},
        {"title": "Zomato Delivery Partner", "salary": "₹ 15000 - 25000", "exp": "Fresher", "cat": "Delivery"},
        {"title": "Retail Sales Executive", "salary": "₹ 12000 - 18000", "exp": "1-3 Year(s)", "cat": "Sales"},
        {"title": "Private Car Driver", "salary": "₹ 15000 - 20000", "exp": "5+ Year(s)", "cat": "Drivers"},
        {"title": "Global Security Ltd", "salary": "₹ 10000 - 15000", "exp": "0-3 Year(s)", "cat": "Security"},
        {"title": "Cap Roof Contractors", "salary": "₹ 12000 - 16000", "exp": "2-5 Year(s)", "cat": "Roofer"},
        {"title": "TOT Hygiene Cleaners", "salary": "₹ 7000 - 11000", "exp": "0-2 Year(s)", "cat": "Cleaner"},
        {"title": "myTVS Mechanic", "salary": "₹ 12000 - 20000", "exp": "3+ Year(s)", "cat": "Mechanic"},
        {"title": "Green Garden Services", "salary": "₹ 8000 - 12000", "exp": "1-4 Year(s)", "cat": "Gardener"},
        {"title": "Elite Elevator Tech", "salary": "₹ 18000 - 25000", "exp": "2-6 Year(s)", "cat": "Elevator"}
    ]

    for job in job_listings:
        if filter_category and job["cat"] != filter_category: continue
        card = tk.Frame(scrollable_frame, bg="white", highlightthickness=1, highlightbackground="#ddd", padx=15, pady=15)
        card.pack(fill="x", padx=15, pady=5)
        tk.Label(card, text=job["title"], font=("Arial", 13, "bold"), bg="white", fg="#2f2f4f").grid(row=0, column=0, sticky="w")
        tk.Label(card, text=job["salary"], font=("Arial", 11, "bold"), bg="white", fg="green").grid(row=0, column=1, sticky="e")
        tk.Label(card, text="🏠 Verified Employer", font=("Arial", 10), bg="white", fg="grey").grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(card, text="📍 Various Locations, India", font=("Arial", 9), bg="white", fg="grey").grid(row=2, column=0, sticky="w")
        tk.Label(card, text="Interview k liye Call kare", font=("Arial", 10, "bold"), bg="white", fg="#444").grid(row=3, column=0, sticky="w", pady=5)
        
        tag_frame = tk.Frame(card, bg="white")
        tag_frame.grid(row=4, column=0, columnspan=2, sticky="w")
        tags = [job["cat"], "On Site", job["exp"]]
        for t in tags:
            tk.Label(tag_frame, text=t, font=("Arial", 8), bg="#f0f0f0", padx=5, pady=2).pack(side="left", padx=2)
        tk.Button(card, text="Apply", bg="white", fg="#e91e63", font=("Arial", 10, "bold"), 
                  relief="ridge", width=10).grid(row=5, column=0, sticky="w", pady=10)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    create_bottom_nav()

# --- PAGE: MAIN HOME ---
def show_main_page():
    clear_screen()
    root.configure(bg="#f5f5f5")
    header = tk.Frame(root, bg="white", pady=10)
    header.pack(fill="x")
    tk.Label(header, text="For Ironhands", font=("Arial", 20, "bold"), fg="#6a1b9a", bg="white").pack()
    
    btn_frame = tk.Frame(root, bg="#f5f5f5", pady=10)
    btn_frame.pack()
    tk.Button(btn_frame, text="Looking for a job", bg="#e91e63", fg="white", width=18, height=2).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="I want to hire", bg="white", fg="#e91e63", width=18, height=2, relief="groove", command=show_hire_popup).grid(row=0, column=1, padx=5)
    
    # --- SEARCH SECTION ---
    search_frame = tk.Frame(root, bg="#2f2f4f", padx=15, pady=15)
    search_frame.pack(padx=15, pady=15, fill="x")
    
    role_text = "role eg:painter"
    role_entry = tk.Entry(search_frame, width=30, font=("Arial", 12), fg="grey")
    role_entry.insert(0, role_text)
    role_entry.bind('<FocusIn>', lambda e: on_entry_click(e, role_text))
    role_entry.bind('<FocusOut>', lambda e: on_focusout(e, role_text))
    role_entry.pack(pady=5)

    loc_text = "location"
    loc_entry = tk.Entry(search_frame, width=30, font=("Arial", 12), fg="grey")
    loc_entry.insert(0, loc_text)
    loc_entry.bind('<Button-1>', lambda e: show_location_selection(loc_entry))
    loc_entry.pack(pady=5)

    tk.Button(search_frame, text="Search Live Jobs", bg="#e91e63", fg="white", width=25, height=2, command=lambda: show_jobs_page()).pack(pady=10)
    
    category_frame = tk.LabelFrame(root, text="Search Jobs By Interest", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
    category_frame.pack(padx=15, pady=10, fill="both", expand=True)
    categories = ["Electrician", "Plumber", "Carpenter", "Warehouse", "Painter", "Delivery", "Sales", "Drivers", "Security","Welders","Roofer","Cleaner","Mechanic","Gardener","Elevator"]
    row, col = 0, 0
    for cat in categories:
        tk.Button(category_frame, text=cat, width=12, height=3, relief="ridge", 
                  command=lambda c=cat: show_jobs_page(c)).grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col > 2: col = 0; row += 1
    create_bottom_nav()

# --- RECRUITER / LOGIN SECTIONS ---
def show_recruiter_home_page():
    clear_screen()
    root.configure(bg="white")
    header = tk.Frame(root, bg="white", pady=10)
    header.pack(fill="x")
    tk.Button(header, text="←", font=("Arial", 14), bd=0, bg="white", command=show_main_page).place(x=10, y=5)
    tk.Label(header, text="For Ironhands", font=("Arial", 20, "bold"), fg="#6a1b9a", bg="white").pack()
    banner = tk.Frame(root, bg="#d0e7ff", padx=15, pady=15)
    banner.pack(padx=15, pady=10, fill="x")
    tk.Label(banner, text="Why Hire with For Ironhands?", font=("Arial", 12, "bold"), bg="#d0e7ff", fg="#2f2f4f").pack(anchor="w")
    points = ["• Easy to Use", "• Start with free credits", "• Cost Effective", "• Hire nearby candidates"]
    for p in points: tk.Label(banner, text=p, font=("Arial", 9), bg="#d0e7ff").pack(anchor="w")
    tk.Entry(root, font=("Arial", 14), fg="grey", bd=0, highlightthickness=1, highlightbackground="#ddd").pack(pady=20, padx=40, fill="x")
    tk.Button(root, text="Login/Register - Recruiter", bg="#cccccc", fg="white", font=("Arial", 12, "bold"), height=2, state="disabled").pack(pady=10, padx=40, fill="x")
    create_bottom_nav()

# UPDATED: Phone Number is now an Entry field
def show_login_popup():
    login_pop = tk.Toplevel(root)
    login_pop.overrideredirect(True)
    width, height = 350, 550
    x, y = root.winfo_x() + 25, root.winfo_y() + 50
    login_pop.geometry(f"{width}x{height}+{x}+{y}")
    login_pop.configure(bg="white")
    
    tk.Button(login_pop, text="←", font=("Arial", 14), bd=0, bg="white", command=login_pop.destroy).place(x=10, y=10)
    tk.Label(login_pop, text="For Ironhands", font=("Arial", 26, "bold"), fg="#2f2f4f", bg="white").pack(pady=(60, 0))
    
    # NEW: Phone Number Input Field (Not a button)
    phone_text = "Phone Number"
    phone_entry = tk.Entry(login_pop, font=("Arial", 12), fg="grey", bd=1, relief="solid", justify="center")
    phone_entry.insert(0, phone_text)
    phone_entry.bind('<FocusIn>', lambda e: on_entry_click(e, phone_text))
    phone_entry.bind('<FocusOut>', lambda e: on_focusout(e, phone_text))
    phone_entry.pack(pady=(40, 10), padx=40, ipady=12, fill="x")
    
    # Existing Login Button
    tk.Button(login_pop, text="Login As a Jobseeker", bg="#cccccc", fg="white", font=("Arial", 12, "bold"), 
              width=25, height=2, bd=0).pack(pady=10)

def show_hire_popup():
    popup = tk.Toplevel(root)
    popup.overrideredirect(True)
    width, height = 320, 240
    x, y = root.winfo_x() + 40, root.winfo_y() + 200
    popup.geometry(f"{width}x{height}+{x}+{y}")
    popup.configure(bg="white", highlightbackground="#e91e63", highlightthickness=2)
    tk.Button(popup, text="No, I am looking for a job", font=("Arial", 10, "bold"), fg="#e91e63", bg="white", width=25, pady=8, command=lambda: [popup.destroy(), show_login_popup()]).pack(pady=40)
    tk.Button(popup, text="Yes, I want to hire staff", font=("Arial", 10, "bold"), fg="#e91e63", bg="white", width=25, pady=8, command=lambda: [popup.destroy(), show_recruiter_home_page()]).pack()

def create_bottom_nav():
    bottom = tk.Frame(root, bg="white", pady=10)
    bottom.pack(side="bottom", fill="x")
    tk.Button(bottom, text="Home", width=8, command=show_main_page).pack(side="left", expand=True)
    tk.Button(bottom, text="Jobs", width=8, command=show_jobs_page).pack(side="left", expand=True)
    tk.Button(bottom, text="Login", width=8, command=show_login_popup).pack(side="left", expand=True)

# --- RUN APP ---
root = tk.Tk()
root.title("For Ironhands")
root.geometry("400x750")
show_main_page()
root.mainloop()
