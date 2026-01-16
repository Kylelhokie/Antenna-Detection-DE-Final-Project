import RPi.GPIO as GPIO
import time

# GPIO pins
STEP = 17  # Connects to PUL- on driver (pin 11)
DIR = 27   # Connects to DIR- on driver (pin 13)

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

print("Stepper Motor Test Starting...")
print("Press Ctrl+C to stop")

def step_motor(steps, delay):
    """Send step pulses to the motor"""
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)

try:
    # Test 1: Slow rotation forward
    print("\nTest 1: Rotating forward (slow)...")
    GPIO.output(DIR, GPIO.LOW)
    step_motor(200, 0.01)  # 200 steps = 1 full rotation, 10ms delay
    time.sleep(1)
    
    # Test 2: Slow rotation backward
    print("Test 2: Rotating backward (slow)...")
    GPIO.output(DIR, GPIO.HIGH)
    step_motor(200, 0.01)
    time.sleep(1)
    
    # Test 3: Faster rotation forward
    print("Test 3: Rotating forward (faster)...")
    GPIO.output(DIR, GPIO.LOW)
    step_motor(400, 0.005)  # 2 rotations, 5ms delay
    time.sleep(1)
    
    # Test 4: Faster rotation backward
    print("Test 4: Rotating backward (faster)...")
    GPIO.output(DIR, GPIO.HIGH)
    step_motor(400, 0.005)
    
    print("\nTest complete! Motor should have rotated.")
    
except KeyboardInterrupt:
    print("\n\nTest stopped by user")
    
finally:
    GPIO.cleanup()
    print("GPIO cleaned up. Exiting.")