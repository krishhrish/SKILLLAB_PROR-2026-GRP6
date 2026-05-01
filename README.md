# SKILL LAB PRATICAL HACKATHON

## Final Project README

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`SKILLLAB_PROR-2026-TeamName`

### Example

`SKILLLAB_PROR-2026-AuroWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name

`RoboNova`

## 1.2 Team Members

| Name                  | Primary Role                    | Secondary Role   | Strengths Brought to the Project |
| --------------        | ------------------------------- | --------------   | -------------------------------- |
| `Hrishikesh Kumbhar ` | `[Ideation,assigning task ]`    | `testing and interfacing sensor `  | `Integration of system,soldering `|
| `Nandini Sondkar `    |  `[Testing and Interfacing sensor,Documentation]` | `Ideation`    |`Repo management and sensor interfacing`
| `Shreenidhi Dumbre`   | `[Raspi setup,web server integration,sensor implemntation]`|`[]Ideation and documentation`|`Basic coding,hardware integration,debugging`|
## 1.3 Project Title

`"Dual Mode Intelligent Robo Car with Obstacle Detection and OLED Monitoring"`

`(because Project-or)`

<img width="1600" height="1131" alt="image" src="https://github.com/user-attachments/assets/c64bfbd4-b3b7-43d9-83ad-c203a5aa11bc" />

## 1.4 One-Line Pitch

`An IoT-based dual mode robo car capable of autonomous obstacle avoidance and real-time web-controlled navigation with smart sensor integration`

## 1.5 Expanded Project Idea

In 1–2 paragraphs, explain:

- what your project is,
- what kind of experience it creates,
- what technologies are involved.

**Response:**  
`Our project is a dual mode smart robo car that can operate in both manual and autonomous modes. In manual mode, the car is controlled through a web-based interface where the user can move the vehicle forward, backward, left, right, and stop it remotely in real time. In autonomous mode, the robo car uses IR sensors to detect obstacles and automatically avoid collisions while navigating. An MPU sensor is used to monitor motion and orientation values, which are displayed live on an OLED display mounted on the vehicle. The system also includes touch sensors that automatically control the headlights, adding smart functionality and improving user interaction.
The project creates an interactive and intelligent driving experience by combining remote vehicle control, sensor-based automation, and real-time monitoring into one compact system. It demonstrates the practical application of embedded systems, automation, and sensor integration in smart vehicle technology. The technologies used in this project include microcontrollers, embedded programming, IR sensors, MPU motion sensors, OLED display modules, touch sensors, motor drivers, and wireless web-based communication for remote control operations.
`

---

# 2. Inspiration

## 2.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `[Video]`   | `https://www.instagram.com/reel/DW4CT7WCDry/?igsh=cXg3dzAxYmdncDBo` | `How projection mapping can be used to create interactive digital + physical experiences` |
|             |                                                                     |                                                                                           |
|             |                                                                     |                                                                                           |

## 2.2 Original Twist

What makes your project original?

**Response:**  
Our project introduces a unique combination of manual web-based control and autonomous navigation within a single robo car system. Unlike basic obstacle-avoiding robots, this system allows users to seamlessly switch between manual driving and automatic obstacle detection modes according to the situation. The integration of an MPU sensor with live OLED display monitoring provides real-time motion and orientation feedback, making the system more interactive and informative.
Another innovative aspect of the project is the use of touch sensors for automatic headlight control, which adds smart automation features similar to modern intelligent vehicles. By combining multiple sensors, real-time monitoring, and dual operational modes into one compact platform, the project demonstrates an advanced and practical approach to smart robotic vehicle design.


---

# 3. Project Intent

## 3.1 User Journey 

Describe exactly how a user will use the project.Make it a story
**Response:**  
A user begins by powering on the robo car system. Once the system starts, the OLED display shows the live MPU sensor values and system status. The user opens the web control interface on a mobile phone or laptop and connects to the robo car. Using the control buttons on the website, the user can move the car forward, backward, left, right, or stop it in real time, creating an interactive remote-driving experience.
While driving manually, the user can observe the motion and orientation changes displayed on the OLED screen. If the user wants the vehicle to operate independently, the system can be switched to autonomous mode. In this mode, the robo car uses IR sensors to detect nearby obstacles and automatically changes direction to avoid collisions without human intervention. During operation, the touch sensors automatically activate the headlights when needed, improving the smart functionality of the vehicle. The entire experience gives the user the feeling of controlling an intelligent mini vehicle capable of both human-controlled and self-navigated movement.

---

# 4. Definition of Success

## 4.1 Definition of “Usable”
The project will be considered “usable” when the robo car is able to successfully operate in both manual and autonomous modes without major errors. In manual mode, the user should be able to control the movement of the car through the web interface in real time with smooth responses for forward, backward, left, right, and stop actions. In autonomous mode, the car should accurately detect obstacles using IR sensors and avoid collisions by changing its path automatically.
The system will also be considered usable when the MPU sensor values are displayed correctly on the OLED screen and the touch sensor-based headlights function properly during operation. A successful user experience means the system responds quickly, operates reliably, and allows seamless switching between manual and automatic modes while maintaining stable vehicle movement and sensor performance.



## 4.2 Minimum Usable Version

What is the smallest version of this project that still delivers the core experience?

**Response:**  
The minimum usable version of the project is a robo car capable of basic movement in both manual and autonomous modes. In manual mode, the user should be able to control the car through the web interface with essential commands such as forward, backward, left, right, and stop. In autonomous mode, the IR sensor should detect obstacles and automatically change the direction of the vehicle to avoid collisions. The motor driver, microcontroller, and wireless communication system must function properly to provide smooth vehicle operation

## 4.3 Stretch Features

What features are nice to have but not essential?


---

# 5. System Overview

## 5.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [x] Sensor-based

- [x] App-connected

- [x] Motorized

- [ ] Sound-based

- [ ] Light-based

- [x] Screen/UI-based

- [ ] Fabricated structure

- [ ]  Game logic based

- [ ] Installation

- [ ] Other:

## 5.2 High-Level System Description

Explain how the system works in simple terms.

Include:

- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
Input
The inputs of the system include commands given by the user through the web-based control interface and data collected from the sensors mounted on the robo car. The user can control the movement of the vehicle using commands such as forward, backward, left, right, and stop, while the IR and MPU sensors continuously provide environmental and motion-related data.
Processing
The microcontroller acts as the main processing unit of the system. It receives user commands and sensor data, then processes the information to control the motors, perform obstacle avoidance, display MPU values on the OLED screen, and manage automatic headlight operation.
Output
The outputs of the system include the movement of the robo car, automatic obstacle avoidance actions, and the display of real-time MPU sensor values on the OLED screen. The system also activates the headlights automatically through the touch sensor mechanism when required.
Physical Structure
The physical structure consists of a robotic car chassis fitted with motors, wheels, sensors, an OLED display, headlights, and a microcontroller. All the components are compactly mounted on the vehicle to ensure stable movement and proper functioning of the system.
App / Website Interaction
The user interacts with the robo car through a web-based interface opened on a mobile phone or laptop. The website allows the user to remotely control the vehicle in real time and switch between manual and autonomous operating modes.




## 5.3 Input / Output Map

| System Part                              | Type            | What It Does                                                                       |
|------------------------------------------|-----------------|------------------------------------------------------------------------------------|
|Web Control Interface	                   |Input	           | Sends movement commands such as forward, backward, left, right, and stop to the robo|
|IR Sensor	                               |Input	           |Detects obstacles in front of the vehicle for autonomous navigation and collision avoidance.|
|MPU Sensor	                               |Input	           |Measures motion and orientation values of the robo car during movement.|
|Touch Sensor	|Input	|Detects touch input to control the automatic headlight system|
|Microcontroller	|Processing	|Processes user commands and sensor data to control the overall operation of the system|
|Motor Driver	|Processing	|Controls the speed and direction of the motors based on signals from the microcontroller|
|DC Motors	|Output	|Moves the robo car in different directions according to user commands or autonomous decisions.
|OLED Display	|Output	|Displays real-time MPU sensor values and system status information.|

---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
<img width="2475" height="863" alt="FINNNNAL BLOCK" src="https://github.com/user-attachments/assets/3442e4ce-6904-4633-8486-c57da29191db" />


Example:

```md

```



## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
<img width="1838" height="2813" alt="FINAL FLOWCHART" src="https://github.com/user-attachments/assets/a45f64dd-b29c-4671-b3b5-fe5fc1d0f02a" />

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 7. Electronics Planning

## 7.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------:| ------------------------------------- |
|Raspberry Pi	|1	|Control|
|OLED Display	|1	|Display|
|MPU Sensor	|1	|Monitoring|
|IR Sensor	|2	|Detection|
|Touch Sensor	|1	|Activation|
|Lithium Battery	|2|	Power|
|Car Chassis Setup	|1|	Movement|
|Arduino uno          |  1|               Control|


## 7.2 Wiring Plan

Describe the main electrical connections.

**sample Response:**  
`Use the Raspberry Pi 3 Model B as the central node: connect both the MPU and the OLED on the same I²C bus (SDA to GPIO2, SCL to GPIO3, plus 3.3 V and GND), ensuring they share common ground and have proper pull-ups if needed; then connect the Pi to the Arduino Uno via UART (Pi TX to Arduino RX, Pi RX to Arduino TX, and a shared GND, with level shifting if required); from the Arduino, wire digital/PWM output pins to the input pins of the L298N motor driver module (e.g., IN1–IN4 and ENA/ENB for speed control), connect the motor leads to the driver’s output terminals, and power the motor driver using an external supply suited to the motor while feeding the Arduino through its VIN or 5 V pin and the Pi through a stable 5 V source, making sure all components share a common ground reference for reliable communication.`

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Lithium-ion Battery Pack`                                                                                                                           |
| Voltage required | `~5V for Raspberry Pi, 3.3V for sensors,5.5v for Arduino and higher voltage supplied to motors through motor driver`                                                                  |
| Current concerns | `Motors may draw high current during movement, which can affect Raspberry Pi stability and sensor performance`                                       |

| Safety concerns  | `Ensure proper voltage regulation, avoid battery over-discharge, prevent short circuits, and maintain secure wiring connections` |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
|Python|	Programming|
|Raspberry Pi OS|	Execution|
Flask / Web |Interface	Control|
 

## 8.2 Software Logic/Algorithm

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`Startup behavior:
The Raspberry Pi initializes the GPIO pins, OLED display, MPU sensor, IR sensors, touch sensor, and motor driver during startup. The system then starts the web server and prepares the robo car for manual or autonomous operation.
Input handling:
The robo car receives movement commands such as forward, backward, left, right, and stop from the web-based control interface. The system also continuously accepts input data from the IR sensors, MPU sensor, and touch sensor.
Sensor reading:
The IR sensors continuously monitor obstacles in front of the vehicle, while the MPU sensor reads motion and orientation values in real time. The touch sensor detects user interaction for automatic headlight control.
Decision logic:
In manual mode, the Raspberry Pi directly executes the movement commands received from the website. In autonomous mode, the system analyzes IR sensor data and automatically changes the direction of the robo car to avoid collisions and maintain movement.
Output behavior:
The motor driver controls the BO motors to move the robo car according to user commands or autonomous decisions. The OLED display shows real-time MPU values and system status, while the headlights activate automatically through the touch sensor mechanism.
Communication logic:
The web interface communicates with the Raspberry Pi through wireless communication. User commands from the mobile phone or laptop are transmitted to the Raspberry Pi, which processes and executes the required actions.


- **Sample Startup behavior:**  
  The Raspi/FPGA initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| Raspberry Pi 3 Model B	|1|	Yes	|No|	0|	40-pin SBC|	Main controller, handles web interface|
|Arduino Uno|	1	|Yes|	No|	0	|ATmega328P|	Real-time motor + sensor control|
|L298N Motor Driver Module|	1	|Yes|	No	|0	|Dual H-Bridge	|Drives 2 DC motors|
|BO DC Motors + Wheels	|4|	yes|	No	|0|	6V high torque	|For movement|
|Motor Shield (if separate)|	1	|Yes|	No	|0|	Arduino compatible|	Easier wiring (optional if L298N used)|
|IR Sensor Module|	1	|Yes|	No|	0	|Obstacle detection	|Input to Arduino|
|OLED Display (I2C)|	1|	No|	Yes |	290	|0.96" SSD1306|	Output display via Pi|
|Li-ion Battery Pack + Holder	|1|	No|	Yes	|200	|7.4V/11.1V	|Portable power supply|
|Power Supply Module	|1	|yes|	No|	0	|Regulated|	Distributes power|


## 9.2 Material Justification

Explain why you selected your main materials and components.

**Response:**  
`The Raspberry Pi 3 Model B was selected as the main controller because it provides sufficient processing capability, GPIO support, and wireless communication features required for handling sensors, web-based control, and autonomous navigation simultaneously. 
The OLED display was chosen because it is compact, power efficient, and capable of displaying real-time MPU sensor values and system status clearly. 
The MPU6050 sensor was selected for accurate motion and orientation monitoring during vehicle movement. 
IR sensors were used for obstacle detection because they are simple, cost-effective, and reliable for short-range autonomous navigation. The touch sensor was included to implement automatic headlight activation and improve the smart functionality of the robo car. 
BO motors with wheels were chosen because they provide sufficient torque and smooth continuous rotation required for vehicle movement. The L298N motor driver module was used to enable bidirectional motor control and stable operation of the motors through the Raspberry Pi. The Arduino Uno was incorporated as a secondary controller to handle real-time motor control and low-level interfacing tasks, reducing the processing load on the Raspberry Pi and ensuring faster, more reliable response for movement operations.
Lithium-ion batteries were selected due to their rechargeable nature, portability, and ability to provide stable power for the entire system.
`


## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| Raspberry Pi 3 Model B|	Main controller, handles web interface|-|-|used|
|Arduino Uno	|Real-time motor and sensor control|-|used|
|L298N Motor Driver Module	|Drives DC motors and controls direction/speed|-|-|used|
|BO Motors + Wheels	|Drive system for car|-|-|used|
|Motor Shield (if separate)	|Simplifies motor connections|-|-|used|
|IR Sensor Module	|Obstacle detection input|-|-|used|
|Touch Sensor Module|	Detects user touch input for control/interaction|-|-|used|
|OLED Display (I2C)	|Displays system output|-|-|used|
|Buck Converter	|Stable 5V supply for Raspberry Pi and Arduino|-|-|used|
|Li-ion Batteries + Holder	|Portable power supply|-|-|used|
|Power Supply Module|	Distributes regulated power|-|-|used|


## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Raspberry Pi 3 Model B|0|
|Arduino Uno|0|
|L298N Motor Driver Module|0|
|BO DC Motors + Wheels|0|
|Motor Shield (if separate)|0|
|IR Sensor Module|0|
|OLED Display (I2C)|0|
|Li-ion Battery Pack + Holder|0|
|Touch Sensor|0|
|Power Supply Module|0|
                                  

## 9.5 Budget Reflection

If your cost to high, what can be simplified,removed,substituted or shared?

**Response:**  
Since all the components were already available the project didnt incure any additional cost .The system was designed to be low cost.

---

# 10. Planning the Work

## 10.1 Team Working Agreement

Write how your team will work together.


Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
Our team consisted of three members, and tasks were divided based on key functional areas of the project. The work was categorized into sensor interfacing, system integration, web server development, and documentation. Each member was assigned primary responsibility for one area, but all members contributed collaboratively to ensure overall understanding and smooth execution.

Decisions were made through group discussions, where all team members shared their ideas and agreed on the most effective approach. This ensured that decisions were well thought out and mutually accepted.

Progress was regularly checked through informal review sessions, where we discussed completed tasks, identified issues, and planned the next steps. This helped us stay aligned with our project timeline.

If any task was delayed, the team worked together to resolve the issue by redistributing work or assisting the concerned member. This ensured that delays did not significantly impact the overall progress of the project.

Documentation was maintained collectively by all team members. Each part of the project was recorded alongside development, and regular updates were made to ensure accuracy and completeness of the final report.

Overall, our team followed a cooperative and flexible working approach, which helped in successfully completing the project.


## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Concept              | `[ALL]`  | `[-]`     |
| Electronics          | `[Hrishikesh]`           | `[Nandini,shreenidhi]`          |
| Coding               | `[Shreenidhi]`           | `[Nandini,Hrishikesh]`          |
| Mechanical build     | `[Hrishikesh]`           | `[Nandini,Shreenidhi]`          |
| Testing              | `[All]`           | `[-]`          |
| Documentation        | `[Nandini]`           | `[Hrishikesh,shrineedih]`          |

---

# 11 hour Milestones

## 11.1 8-hour Plan(tentetively you may set)

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [ ] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [x] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [ ] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [x] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Days   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
|10:00–11:30|	Hardware setup & basic connections	|Wiring completed between Raspberry Pi, Arduino, motor driver|	Took time to verify correct pin connections	Recheck and secure all connections|
|11:30–12:30|	Sensor & display interfacing	|MPU connected; display partially working	|Display required extra configuration	Fix display output and test visualization|
|12:30–2:00	|Motor testing & communication setup|	Motors worked; |Arduino–Pi communication established	Inconsistent motor movement; minor code issues|	Calibrate motors and optimize communication
|2:00–4:00	|Control logic & full system testing	|Basic movement achieved; system partially working|	Delays and synchronization issues	Improve logic, debug errors, enhance performance|

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
|WiFi connection between laptop and Raspberry Pi becomes unstable|	Team |Technical	|Medium	|High|	Keep Raspberry Pi close to client device, ensure stable hotspot/WiFi connection, reduce network load, add fail-safe stop|
Serial communication delay between Raspberry Pi and Arduino|	Team|Technical|	Medium|	High|	Optimize baud rate, test UART communication regularly, add error handling in code|
|IR sensors fail to detect obstacles correctly|	Team|Technical|	Medium|	Medium	|Perform proper sensor calibration and testing under different lighting condition|
Loose wiring or connection failure	|Team|Hardware	|Medium	|High	|Secure all jumper wires and connections before testing|



## 13.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  

The biggest uncertainty in the project at this stage is maintaining stable real-time communication and synchronization between the Raspberry Pi, Arduino Uno, web server, and sensors during continuous operation. Since the robotic car depends on serial communication, WiFi connectivity, sensor inputs, and motor control simultaneously, any delay or interruption may affect movement accuracy and autonomous navigation. Another uncertainty is efficient power distribution to the Raspberry Pi, Arduino, motor driver shield, and motors while ensuring stable performance under different load conditions. Further testing is required to improve reliability, response time, and overall system stability.
---

# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Motor movement	|Test forward, backward, left, and right movement	|Motors rotate correctly in all directions|
|IR obstacle detection	|Place obstacles in front of the robo car during autonomous mode	|Car detects and avoids obstacles successfully|
|MPU sensor readings	|Move and tilt the robo car while monitoring |OLED display	OLED displays accurate real-time MPU values|
|OLED display	Verify display during startup and movement	|Sensor values and system status are visible clearly|
|Touch sensor	|Touch the sensor to activate headlights	|Headlights turn ON and OFF correctly|
|Battery performance	|Run the robo car continuously for extended duration	|System operates without sudden shutdowns|
|Mode switching	|Switch between manual and autonomous modes	|System changes modes smoothly without errors

## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
|10:00 AM	|MPU readings not displaying properly on OLED|	Sensor / Software	Checked I2C connections and recalibrated MPU sensor	|Improved	|Fine-tune sensor values
|11:00 AM	|Website controls not responding smoothly	|Frontend	Modified control button handling and refreshed backend connection	|Worked	|Improve UI design|
|12:00 PM	|Delay in car movement after sending commands|	Backend / Communication	Optimized command processing and reduced response delay|	Improved|	Test with multiple devices|
|1:00 PM	|IR sensor not detecting obstacles correctly	Sensor	Adjusted sensor placement and detection range	|Worked partially	|Increase detection accuracy|
|2:00 PM	|Autonomous mode giving unstable turns	|Logic	Updated obstacle avoidance conditions in the code|	Improved|	Perform navigation testing
               |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />





# 17. Final Outcome

## 17.1 Final Description

Describe the final version of your project.

**Response:**  
The final project is a web-controlled 4-wheel drive robotic car built using Raspberry Pi 3B, Arduino Uno, motor driver shield, IR sensors, MPU sensor, touch sensors, OLED display, and DC motors. The Raspberry Pi hosts a web server that allows the user to control the car remotely through a browser interface. Commands are sent serially to the Arduino Uno, which controls the motor driver shield for car movement. The project supports both manual mode and autonomous mode. In autonomous mode, the IR sensors detect obstacles and the car changes direction automatically. Touch sensors are used to control the headlights of the vehicle, improving user interaction and functionality. The MPU sensor provides motion-related data, while the OLED display shows real-time system information and status updates. A battery power supply powers the Raspberry Pi, Arduino Uno, motor driver shield, and DC motors to ensure complete standalone operation.

## 17.2 What Works Well
The web-based manual control works smoothly with low response delay between the client and the robotic car. Serial communication between Raspberry Pi and Arduino is stable during operation. The motor driver shield successfully drives all four DC motors for forward, backward, left, and right movement. The autonomous obstacle detection using IR sensors performs reliably in most indoor environments. The touch sensor-based headlight control works properly and improves usability. The MPU and OLED integration also function correctly and provide useful real-time feedback during testing. The battery supply system efficiently powers the motors, Arduino, and Raspberry Pi during operation.


## 17.3 What Still Needs Improvement

The obstacle detection accuracy can still be improved for complex environments and uneven surfaces. WiFi connectivity occasionally becomes unstable when the distance between the client device and Raspberry Pi increases The system can further be enhanced by adding advanced voice command functionality, and improved sensor calibration for better autonomous performance.
## 17.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  

Initially, the project was planned as a simple web-controlled robotic car with only manual movement control. During development, autonomous obstacle avoidance functionality was added using IR sensors to improve the intelligence of the system. Additional features such as MPU sensor integration, OLED display output, touch sensor-controlled headlights, and battery-powered standalone operation were also included to enhance functionality and user interaction. The project evolved from a basic remote-controlled vehicle into a hybrid smart robotic system capable of both manual and autonomous operation with real-time monitoring features.
---

# 18. Reflection

## 18.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
Our team worked well in dividing tasks such as web server development, sensor interfacing, motor control, and testing. Good communication and regular testing helped us complete the integration successfully. The main challenges were unstable WiFi connectivity, serial communication issues between Raspberry Pi and Arduino, and sensor calibration delays. We managed time and responsibilities effectively by assigning specific modules to each team member and continuously tracking progress

## 18.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  

We learned how to interface Raspberry Pi with Arduino using serial communication and how to control motors using a motor driver shield. We gained experience in web server programming, IR sensor integration, MPU interfacing, and OLED display handling. The project also improved our understanding of embedded systems integration, debugging hardware-software interaction, and power management in robotic systems.
## 18.3 Design Reflection

What did you learn about:

- designing ,
- delight,
- clarity,
- physical interaction,
- understanding,
- iteration?

**Response:**  
We learned the importance of designing a modular and well-structured embedded system where each component performs a specific task efficiently. Clear system architecture and proper component organization made hardware integration, debugging, and testing much easier. While designing the robotic car, we understood how reliability becomes critical in real-time systems because even small communication delays or sensor errors can affect the movement of the vehicle. The project also taught us the value of user-friendly control interfaces, proper power distribution, and efficient wiring management to improve system stability and overall performance. Additionally, we gained experience in balancing both manual web-based control and autonomous obstacle-avoidance functionality within a single integrated system.

## 18.4 If You Had One More hour

What would you improve next?

**Response:**  

`If we had one more hour, we would add a voice command feature to control the robotic car using simple commands such as “forward,” “backward,” “left,” “right,” and “stop.” The voice commands could be processed through a mobile device or integrated with the Raspberry Pi using speech recognition libraries. We would also improve obstacle avoidance accuracy, optimize the web interface for smoother control, and add live sensor status monitoring on the OLED display and web dashboard for better user interaction and system feedback. `

---

# 19. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="" />

---


---


