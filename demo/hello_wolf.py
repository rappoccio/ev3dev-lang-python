import ev3dev.ev3 as ev3
ev3.Sound.speak("OH MY GOSH Wolf. Thank you so much for this gift. I named him Terky.").wait()

mB = ev3.LargeMotor('outB')
mC = ev3.LargeMotor('outC')
for m in [mB, mC] : 
    m.run_timed(time_sp=10000, speed_sp=500)
 
for m in [mB, mC] : 
    m.run_timed(time_sp=10000, speed_sp=-500)

