#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the universe of discourse
dirtiness = ctrl.Antecedent(np.arange(0, 101, 1), 'dirtiness')
load_weight = ctrl.Antecedent(np.arange(0, 11, 1), 'load_weight')
dirt_type = ctrl.Antecedent(np.arange(0, 101, 1), 'dirt_type')
cloth_sensitivity = ctrl.Antecedent(np.arange(0, 101, 1), 'cloth_sensitivity')
water_hardness = ctrl.Antecedent(np.arange(0, 101, 1), 'water_hardness')

wash_time = ctrl.Consequent(np.arange(0, 121, 1), 'wash_time')
spin_speed = ctrl.Consequent(np.arange(0, 1401, 100), 'spin_speed')
water_amount = ctrl.Consequent(np.arange(0, 51, 1), 'water_amount')
detergent_amount = ctrl.Consequent(np.arange(0, 101, 1), 'detergent_amount')
water_temperature = ctrl.Consequent(np.arange(0, 101, 1), 'water_temperature')

# Fuzzy membership functions
dirtiness['clean'] = fuzz.trimf(dirtiness.universe, [0, 0, 50])
dirtiness['average'] = fuzz.trimf(dirtiness.universe, [30, 50, 70])
dirtiness['dirty'] = fuzz.trimf(dirtiness.universe, [60, 70, 80])
dirtiness['very dirty'] = fuzz.trimf(dirtiness.universe, [75, 90, 100])

load_weight['light'] = fuzz.trimf(load_weight.universe, [0, 0, 5])
load_weight['medium'] = fuzz.trimf(load_weight.universe, [3, 5, 7])
load_weight['heavy'] = fuzz.trimf(load_weight.universe, [6, 10, 10])

dirt_type['not greasy'] = fuzz.trimf(dirt_type.universe, [0, 0, 50])
dirt_type['greasy'] = fuzz.trimf(dirt_type.universe, [30, 50, 100])

cloth_sensitivity['low'] = fuzz.trimf(cloth_sensitivity.universe, [0, 0, 50])
cloth_sensitivity['high'] = fuzz.trimf(cloth_sensitivity.universe, [30, 50, 100])

water_hardness['soft'] = fuzz.trimf(water_hardness.universe, [0, 0, 50])
water_hardness['hard'] = fuzz.trimf(water_hardness.universe, [30, 50, 100])

wash_time['very short'] = fuzz.trimf(wash_time.universe, [0, 0, 30])
wash_time['short'] = fuzz.trimf(wash_time.universe, [20, 30, 45])
wash_time['medium'] = fuzz.trimf(wash_time.universe, [40, 60, 80])
wash_time['long'] = fuzz.trimf(wash_time.universe, [70, 90, 110])
wash_time['very long'] = fuzz.trimf(wash_time.universe, [100, 120, 120])

spin_speed['low'] = fuzz.trimf(spin_speed.universe, [0, 0, 700])
spin_speed['medium'] = fuzz.trimf(spin_speed.universe, [500, 900, 1300])
spin_speed['high'] = fuzz.trimf(spin_speed.universe, [1100, 1400, 1400])

water_amount['low'] = fuzz.trimf(water_amount.universe, [0, 0, 25])
water_amount['medium'] = fuzz.trimf(water_amount.universe, [15, 25, 35])
water_amount['high'] = fuzz.trimf(water_amount.universe, [30, 50, 50])

detergent_amount['low'] = fuzz.trimf(detergent_amount.universe, [0, 0, 50])
detergent_amount['medium'] = fuzz.trimf(detergent_amount.universe, [30, 50, 70])
detergent_amount['high'] = fuzz.trimf(detergent_amount.universe, [60, 100, 100])

water_temperature['low'] = fuzz.trimf(water_temperature.universe, [0, 0, 50])
water_temperature['medium'] = fuzz.trimf(water_temperature.universe, [30, 50, 70])
water_temperature['high'] = fuzz.trimf(water_temperature.universe, [60, 100, 100])

# Fuzzy rules
rule1 = ctrl.Rule(dirtiness['very dirty'] & load_weight['heavy'], 
                  [wash_time['very long'], spin_speed['high'], water_amount['high'], detergent_amount['high'], water_temperature['high']])
rule2 = ctrl.Rule(dirtiness['dirty'] & load_weight['medium'], 
                  [wash_time['long'], spin_speed['medium'], water_amount['medium'], detergent_amount['medium'], water_temperature['medium']])
rule3 = ctrl.Rule(dirtiness['average'] & load_weight['light'], 
                  [wash_time['medium'], spin_speed['low'], water_amount['medium'], detergent_amount['medium'], water_temperature['medium']])
rule4 = ctrl.Rule(dirtiness['clean'] & load_weight['light'], 
                  [wash_time['short'], spin_speed['low'], water_amount['low'], detergent_amount['low'], water_temperature['low']])
rule5 = ctrl.Rule(dirt_type['not greasy'] & cloth_sensitivity['low'] & water_hardness['soft'],
                  [wash_time['short'], spin_speed['low'], water_amount['medium'], detergent_amount['low'], water_temperature['medium']])
rule6 = ctrl.Rule(dirt_type['not greasy'] & cloth_sensitivity['high'] & water_hardness['soft'],
                  [wash_time['medium'], spin_speed['medium'], water_amount['high'], detergent_amount['medium'], water_temperature['medium']])
rule7 = ctrl.Rule(dirt_type['not greasy'] & cloth_sensitivity['low'] & water_hardness['hard'],
                  [wash_time['short'], spin_speed['medium'], water_amount['low'], detergent_amount['low'], water_temperature['medium']])
rule8 = ctrl.Rule(dirt_type['not greasy'] & cloth_sensitivity['high'] & water_hardness['hard'],
                  [wash_time['medium'], spin_speed['high'], water_amount['medium'], detergent_amount['medium'], water_temperature['high']])
rule9 = ctrl.Rule(dirt_type['greasy'] & cloth_sensitivity['low'] & water_hardness['soft'],
                  [wash_time['long'], spin_speed['low'], water_amount['medium'], detergent_amount['medium'], water_temperature['medium']])
rule10 = ctrl.Rule(dirt_type['greasy'] & cloth_sensitivity['high'] & water_hardness['soft'],
                  [wash_time['long'], spin_speed['medium'], water_amount['high'], detergent_amount['high'], water_temperature['high']])
rule11 = ctrl.Rule(dirt_type['greasy'] & cloth_sensitivity['low'] & water_hardness['hard'],
                  [wash_time['long'], spin_speed['medium'], water_amount['low'], detergent_amount['medium'], water_temperature['high']])
rule12 = ctrl.Rule(dirt_type['greasy'] & cloth_sensitivity['high'] & water_hardness['hard'],
                  [wash_time['very long'], spin_speed['high'], water_amount['high'], detergent_amount['high'], water_temperature['high']])

# System setup
washing_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12])
washing_machine = ctrl.ControlSystemSimulation(washing_system)

# Tkinter initialization
root = tk.Tk()
root.title("Automatic Washer Control System")

def start_washing():
    # Set inputs to the washing machine system
    washing_machine.input['dirtiness'] = dirtiness_slider.get()
    washing_machine.input['load_weight'] = load_weight_slider.get()
    washing_machine.input['dirt_type'] = dirt_type_slider.get()
    washing_machine.input['cloth_sensitivity'] = cloth_sensitivity_slider.get()
    washing_machine.input['water_hardness'] = water_hardness_slider.get()

    # Compute the outputs
    washing_machine.compute()

    # Update output labels
    wash_time_output.config(text=f"Recommended Wash Time: {washing_machine.output['wash_time']:.1f} minutes.")
    spin_speed_output.config(text=f"Recommended Spin Speed: {washing_machine.output['spin_speed']:.1f} RPM.")
    water_amount_output.config(text=f"Water Amount: {washing_machine.output['water_amount']:.1f} Litres.")
    detergent_amount_output.config(text=f"Detergent Amount: {washing_machine.output['detergent_amount']:.1f} ml.") 
    water_temperature_output.config(text=f"Water Temperature: {washing_machine.output['water_temperature']:.1f}°C.")

    # Disable the button after starting
    start_button.config(state=tk.DISABLED)
    
# Define Start Washing button
start_button = ttk.Button(root, text="Start Washing", command=start_washing)
start_button.grid(row=5, column=0, columnspan=3, pady=10)  # Adjust row and column as needed

# Update outputs based on slider values
def update_outputs(event=None):
    # Get slider values for all inputs
    dirtiness_value = dirtiness_slider.get()
    load_weight_value = load_weight_slider.get()
    dirt_type_value = dirt_type_slider.get()
    cloth_sensitivity_value = cloth_sensitivity_slider.get()
    water_hardness_value = water_hardness_slider.get()

    # Update input labels
    dirtiness_value_label.config(text=f"Value: {dirtiness_value:.1f}")
    load_weight_value_label.config(text=f"Value: {load_weight_value:.1f}")
    dirt_type_value_label.config(text=f"Value: {dirt_type_value:.1f}")
    cloth_sensitivity_value_label.config(text=f"Value: {cloth_sensitivity_value:.1f}")
    water_hardness_value_label.config(text=f"Value: {water_hardness_value:.1f}")


# Define sliders for inputs
dirtiness_label = ttk.Label(root, text="Dirtiness Level(0 Clean to 100 Dirty):", anchor=tk.W)
dirtiness_slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_outputs)
dirtiness_value_label = ttk.Label(root, text=f"Dirtiness Value: {int(dirtiness_slider.get())}", anchor=tk.W)

load_weight_label = ttk.Label(root, text="Load Weight (kg):", anchor=tk.W)
load_weight_slider = ttk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, length=200, command=update_outputs)
load_weight_value_label = ttk.Label(root, text=f"Load Weight Value: {int(load_weight_slider.get())}", anchor=tk.W)

dirt_type_label = ttk.Label(root, text="Dirt Type (0 not greasy to 100 greasy):", anchor=tk.W)
dirt_type_slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_outputs)
dirt_type_value_label = ttk.Label(root, text=f"Dirt Type Value: {int(dirt_type_slider.get())}", anchor=tk.W)

cloth_sensitivity_label = ttk.Label(root, text="Cloth Sensitivity (0 low to 100 high):", anchor=tk.W)
cloth_sensitivity_slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_outputs)
cloth_sensitivity_value_label = ttk.Label(root, text=f"Cloth Sensitivity Value: {int(cloth_sensitivity_slider.get())}", anchor=tk.W)

water_hardness_label = ttk.Label(root, text="Water Hardness (0 soft to 100 hard):", anchor=tk.W)
water_hardness_slider = ttk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=update_outputs)
water_hardness_value_label = ttk.Label(root, text=f"Water Hardness Value: {int(water_hardness_slider.get())}", anchor=tk.W)


# Define labels for outputs
output_label = ttk.Label(root, text="Outputs:", anchor=tk.W)
wash_time_output = ttk.Label(root, text="Recommended Wash Time:", anchor=tk.W)
spin_speed_output = ttk.Label(root, text="Recommended Spin Speed:", anchor=tk.W)
water_amount_output = ttk.Label(root, text="Recommended Water Amount:", anchor=tk.W)
detergent_amount_output = ttk.Label(root, text="Recommended Detergent Amount:", anchor=tk.W)
water_temperature_output = ttk.Label(root, text="Recommended Water Temperature:", anchor=tk.W)

# Layout widgets
dirtiness_label.grid(row=0, column=0, sticky=tk.W)
dirtiness_slider.grid(row=0, column=1, sticky=tk.W+tk.E)
dirtiness_value_label.grid(row=0, column=2, sticky=tk.W)

load_weight_label.grid(row=1, column=0, sticky=tk.W)
load_weight_slider.grid(row=1, column=1, sticky=tk.W+tk.E)
load_weight_value_label.grid(row=1, column=2, sticky=tk.W)

dirt_type_label.grid(row=2, column=0, sticky=tk.W)
dirt_type_slider.grid(row=2, column=1, sticky=tk.W+tk.E)
dirt_type_value_label.grid(row=2, column=2, sticky=tk.W)

cloth_sensitivity_label.grid(row=3, column=0, sticky=tk.W)
cloth_sensitivity_slider.grid(row=3, column=1, sticky=tk.W+tk.E)
cloth_sensitivity_value_label.grid(row=3, column=2, sticky=tk.W)

water_hardness_label.grid(row=4, column=0, sticky=tk.W)
water_hardness_slider.grid(row=4, column=1, sticky=tk.W+tk.E)
water_hardness_value_label.grid(row=4, column=2, sticky=tk.W)

# Outputs layout
output_label.grid(row=5, column=0, columnspan=3, sticky=tk.W)
wash_time_output.grid(row=6, column=0, columnspan=3, sticky=tk.W)
spin_speed_output.grid(row=7, column=0, columnspan=3, sticky=tk.W)
water_amount_output.grid(row=8, column=0, columnspan=3, sticky=tk.W)
detergent_amount_output.grid(row=9, column=0, columnspan=3, sticky=tk.W)
water_temperature_output.grid(row=10, column=0, columnspan=3, sticky=tk.W)

# responsiveness
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Update outputs
update_outputs()

# Show the GUI
root.mainloop()


# In[ ]:





# In[ ]:




