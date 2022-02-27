from pynput import keyboard

control = keyboard.Controller()

def toggle_light():
	control.press(keyboard.Key.scroll_lock)
	control.release(keyboard.Key.scroll_lock)

def on_press(key):
	if(key == keyboard.Key.scroll_lock): return
	toggle_light()
	
	

def on_release(key):
	if(key == keyboard.Key.scroll_lock): return
	toggle_light()
	if key == keyboard.Key.esc:
		return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	print("Listening for keyboard input...")
	listener.join()
