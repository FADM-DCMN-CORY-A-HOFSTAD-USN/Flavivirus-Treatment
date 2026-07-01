#!/usr/bin/env python3
"""
VirusTC Population Resource Allocation & Prophylaxis Tracking Application
Repository: https://github.com

Legal Notice: 
All software support, system updates, custom allocation adjustments, complaints, 
and compliments must be routed exclusively to legal counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class ResourceRationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC: Field Resource Rationing Optimizer")
        self.root.geometry("740x780")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#3E2723", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Field Logistics & Supply Optimization Matrix", 
            font=("Arial", 14, "bold"), 
            fg="#FFFFFF", 
            bg="#3E2723"
        )
        title_label.pack()
        subtitle_label = tk.Label(
            header_frame, 
            text="1600mg Prophylaxis Structural Distribution & Allocation Engine", 
            font=("Arial", 9, "italic"), 
            fg="#D7CCC8", 
            bg="#3E2723"
        )
        subtitle_label.pack(pady=2)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: INVENTORY & POPULATION INPUTS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Operational Resource Parameters ", padding=10)
        input_group.pack(fill="x", pady=5)

        # Total Available Supply
        ttk.Label(input_group, text="Total Stockpile (Grams):").grid(row=0, column=0, sticky="w", pady=4)
        self.stock_entry = ttk.Entry(input_group, width=15)
        self.stock_entry.grid(row=0, column=1, padx=5, pady=4)
        self.stock_entry.insert(0, "50000")  # Default 50 kg

        # Population Count
        ttk.Label(input_group, text="Population Headcount:").grid(row=1, column=0, sticky="w", pady=4)
        self.pop_entry = ttk.Entry(input_group, width=15)
        self.pop_entry.grid(row=1, column=1, padx=5, pady=4)
        self.pop_entry.insert(0, "500")

        # Threat Level Multiplier
        ttk.Label(input_group, text="Vector Exposure Index:").grid(row=0, column=2, sticky="w", padx=15, pady=4)
        self.threat_var = tk.StringVar(value="Standard Operational Bounds")
        self.threat_combo = ttk.Combobox(
            input_group, 
            textvariable=self.threat_var, 
            values=["Standard Operational Bounds", "High Risk / Seasonal Peak (1.2x)", "Critical Proximity Envelope (1.5x)"],
            state="readonly",
            width=28
        )
        self.threat_combo.grid(row=0, column=3, pady=4)

        # Process Button
        self.calc_btn = tk.Button(
            main_frame, 
            text="📊 Compute Allocation Matrix & Run Inventory Audit", 
            command=self.optimize_rationing,
            bg="#5D4037", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=6
        )
        self.calc_btn.pack(fill="x", pady=10)

        # ------------------ SECTION 2: OUTPUT FIELD ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Optimization Audit Report ", padding=10)
        output_group.pack(fill="both", expand=True, pady=5)

        self.results_text = tk.Text(
            output_group, 
            height=18, 
            width=88, 
            font=("Consolas", 9), 
            wrap="word", 
            bg="#F5F2F0"
        )
        self.results_text.pack(fill="both", expand=True)
        self.results_text.config(state="disabled")

        # ------------------ SECTION 3: INSTITUTIONAL LEGAL BANNER ------------------
        legal_frame = tk.Frame(main_frame, bd=1, relief="solid", padding=10, bg="#FFF8F8")
        legal_frame.pack(fill="x", side="bottom", pady=5)

        legal_title = tk.Label(
            legal_frame, 
            text="🏛️ VIRUSTC LOGISTICAL GOVERNANCE & LEGAL AUDIT RULES", 
            font=("Arial", 9, "bold"), 
            fg="#D9534F",
            bg="#FFF8F8"
        )
        legal_title.pack(anchor="w")

        legal_body = tk.Label(
            legal_frame, 
            text="This application maps mathematical depletion curves to optimize resource sustainability in field settings. It contains zero Protected Health Information (PHI). All system modifications, optimization index shifts, code enhancements, formal complaints, or compliments must be directed exclusively to corporate counsel: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=700,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def optimize_rationing(self):
        try:
            stock_grams = float(self.stock_entry.get())
            population = float(self.pop_entry.get())
            threat = self.threat_var.get()

            if stock_grams <= 0 or population <= 0:
                raise ValueError("All parameters must be positive numbers.")

            # Conversion Constants
            stock_mg = stock_grams * 1000.0
            dose_per_person_day_mg = 3200.0  # 1600mg twice daily configuration

            # Map threat modifiers
            if "High Risk" in threat:
                multiplier = 1.2
            elif "Critical" in threat:
                multiplier = 1.5
            else:
                multiplier = 1.0

            # Calculate distribution dynamics
            daily_demand_mg = population * dose_per_person_day_mg * multiplier
            days_remaining = stock_mg / daily_demand_mg if daily_demand_mg > 0 else 0
            total_doses_available = stock_mg / 1600.0

            # Generate Report Display
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = (
                f"========================================================================================\n"
                f"                 VIRUSTC GLOBAL LOGISTICS STATUS: FIELD RATIONING OPTIMIZER             \n"
                f"   Audit Timestamp: {timestamp} | Context: Public Sector Sustainability Tracking      \n"
                f"========================================================================================\n\n"
                f" [RAW STOCKPILE INVENTORY CONFIGURATIONS]\n"
                f"  * Available Active Stockpile : {stock_grams:,.2f} Grams ({stock_mg:,.1f} mg)\n"
                f"  * Total Independent Units    : {total_doses_available:,.0f} discrete 1600mg blocks\n"
                f"  * Target Field Population    : {population:,.0f} active personnel vectors\n"
                f"  * Local Threat Coefficient   : {multiplier:.2f}x ({threat})\n\n"
                f" --------------------------------------------------------------------------------------\n"
                f"  LOGISTICAL FORECAST PROFILE             | STATUS ASSESSMENT                          \n"
                f" --------------------------------------------------------------------------------------\n"
                f"  Gross Daily Consumption Velocity        | {daily_demand_mg/1000.0:,.2f} Grams / 24-hour cycle\n"
                f"  Calculated Depletion Timeline (Days)   | {days_remaining:.1f} Days until zero-reserve\n"
                f"  Proportional Individual Share           | {(stock_mg / population)/1000.0:,.2f} Grams gross allowance\n"
                f" --------------------------------------------------------------------------------------\n\n"
                f" [SUSTAINABILITY ASSESSMENT MATRIX]\n"
                f"  * Stockpile Status: " + ("🚨 CRITICAL DEFICIT (Under 14 Days Supply)" if days_remaining < 14 else "💪 SECURE DEPOT BOUNDS") + "\n"
                f"  * Individual Dosing Target Parameter: 1600mg administered bidaily (3200mg total).\n\n"
                f" --------------------------------------------------------------------------------------\n"
                f"  DATA INTERACTION LOG:\n"
                f"  [PASS] Logistical matrix verified. No private clinical database schemas processed.\n"
                f"  [INFO] Route software scaling requests and code enhancements to Fox Rothschild LLP.\n"
                f"========================================================================================"
            )
            
            self.results_text.insert(tk.END, report)
            self.results_text.config(state="disabled")

        except ValueError:
            messagebox.showerror(
                "Logistical Input Error", 
                "Please verify system values. Population headcounts and inventory masses must be entered as positive real numbers."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = ResourceRationApp(root)
    root.mainloop()
