# import keyboard

# # Variable to keep track of the number of times "Esc" key is pressed
# esc_count = 0

# def on_key_press(event):
#     print(f"Key pressed: {event.name}")

#     if event.name == 'esc':
#         # Increment the count if "Esc" key is pressed
#         esc_count += 1

#         # Break the loop if "Esc" key is pressed twice
#         if esc_count >= 2:
#             keyboard.unhook_all()
#             return

#         else:
#         # Reset the count if any other key is pressed
#          esc_count = 0

# keyboard.on_press(on_key_press)


# while True:
#     if keyboard.is_pressed('esc'):
#         break

# print("Program finished.")

# import keyboard

# def on_key_press(event):
#     print(f"Key pressed: {event.name}")

# keyboard.on_press(on_key_press)

# # Keep the program running until 'q' is pressed
# # while True:
# #    if keyboard.is_pressed('esc'):
# #       break
# import keyboard

# # Variable to keep track of the number of times "Esc" key is pressed
# esc_count = 0

# while True:
#     if keyboard.is_pressed('esc'):
#         # Increment the count if "Esc" key is pressed
#         esc_count += 1

#         # Break the loop if "Esc" key is pressed twice
#         if esc_count >= 2:
#             break
#     else:
#         # Reset the count if any other key is pressed
#         esc_count = 0
# while True:
#    if keyboard.is_pressed('esc'):
#       break
   


import keyboard

def on_key_press(event):
    print(f"Key pressed: {event.name}")

keyboard.on_press(on_key_press)

# Keep the program running until 'q' is pressed
while True:
    if keyboard.is_pressed('Scroll Lock'):
        break
