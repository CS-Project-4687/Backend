<p align="center">
<img height="200px" width="auto" src="https://raw.githubusercontent.com/CS-Project-4687/.github/refs/heads/main/DPSLogo.svg">
</p>
<h1 align="center">Delhi Public School Srinagar<br><br><p>Project Synopsis:</p>AI Timetable Creator</h1>
<p>Made By:<br><ol><li>Meesam</li><li>Asad Suhail Shah</li></ol></p>
<h2>1. Acknowledgements</h2>
<p>We would like to take a moment to express our heartfelt gratitude for the unwavering support and dedication of our esteemed Computer Science teacher Javaid Ahmed Sofi. His passion for teaching and his ability to inspire has made a profound impact on our learning journey. He has not only shared knowledge but also instilled confidence in us, encouraging us to pursue our interests and overcome challenges. His patience and understanding have created a safe space for growth, and we truly appreciate the time and effort he invests in each of his students.</p>
<p>We thank him for being a guiding light and for believing in us when we sometimes doubted even ourselves.</p>
<h2>2. Project Outline</h2>
<h3>2.1. Introduction</h3>
<p>The Time Table Creator (TTC) is a web-application that employs the use of AI to allow a user to create a detailed time-table for any amount of tasks that they may have throughout the day with the least amount of work required, saving the most amount of time for the tasks themselves.</p>
<h3>2.2. Objective</h3>
<p>Manually creating a timetable can become extremely repetitive and time-consuming if one is not careful; when there are several subjects and/or events to consider throughout the day, a good chunk of the time that can be spent productively is wasted in planning. The following project attempts to solve that issue by using AI to help create an efficient time-table for you. Instead of having to go through the hard-work of creating a detailed time-table yourself, you can give the AI a simple prompt, and it will do the rest.</p>
<p>It harbors a user-friendly interface to allow ease-of-use, and can factor things like Break and Lunch Times, and other such necessary interruptions that may take place throughout the day.</p>
<p>It can be used by anyone: students, teachers, corporate employees, researchers, and even the general populous for everyday uses.</p>
<p>Saved timetables are stored on the back-end (detailed further), and can be accessed at any time the user wishes.</p>
<h3>2.3. Scope</h3>
<p>The TTC can be used for a range of applications, since the Time-Table it can create can contain as much detail as one requires. That said, as is true with all AI, it can contain errors and misrepresentations of prompts, which limit its applications in the larger industry which requires much more precision. But it can be easily used for everyday applications, such as making a timetable to study, exercise, eat (if you forget doing that sometimes), or gather materials to make a general purpose explosive for research. In those cases, you can trust the results with a high-level of confidence, although going over and tweaking the results is recommended.</p>
<p>Further work on the project (updates and improvements), will allow for wider applications in the general industry, and will be able to provide a much more lucid timetable with much greater precision and reliability, and will make existing systems much faster and easier to manage.</p>
<h3>2.4. The Proposed System</h3>
<p>The system we have proposed is more dependent on the ever growing strength of AI, than on human work. All it requires is a relatively simple prompt from the user, and out comes a detailed timetable telling you exactly what to do throughout the day so that you don’t have to think even once about mundane tasks such as the one it solves. It is resistant to the dynamics of the day since a prompt can be given at any time, at it will adjust the timetable accordingly.</p>
<p>Eventually, once the model is powerful enough, a person may be able to input a prompt and the TTC would tell you exactly what to do throughout the entire day: when to eat, what to eat, when to sleep, when to take a break, what to do in that break, what to do EXACTLY when working and how to work for maximum efficiency, since such thought is not suited for human minds. We must not bog ourselves down with how to manage ourselves and our days. We must not waste time thinking about meaningless things such as privacy and mental autonomy; we must leave the dull and monotonous tasks like planning and thinking to the AI suzerain.</p>
<p>Thought is of no importance. The only thing that matters is work; only work propels our lives further. And that noble goal is achieved by our AI-TTC.</p>
<h2>3. Requirements</h2>
<h3>3.1. Input/Output</h3>
<p>All it requires is a modern device with a screen and a viable form of language input, such as a physical or virtual keyboard</p>
<h3>3.2. Hardware and Software</h3>
<h4>3.2.1. Hardware</h4>
<p>Any modern computer device will be able to run the TTC since it does not have heavy processing requirements.</p>
<p>Mobile phones are discouraged due to the small screen which may cause visual/ orientation issues, and thus, tablets or PCs are preferred. Running this software on a Raspberry Pi may cause runaway atmospheric nuclear fusion</p>
<h4>3.2.2. Software</h4>
<p>There is no preference of software, and this program can be easily run on Windows, Linux and macOS</p>
<h2>4. The Program</h2>
<h3>4.1. System Design</h3>
<h4>4.1.1. The Back-end</h4>
<p>The TTC has been written in python. It creates an API call to an LLM (Large Language Model), which has been tuned to create timetables. The TTC then parses the response of the LLM into a readable and accessible format.</p>
<p>The TTC uses a web-server that responds to POST and GET requests. For the POST requests, input is a required parameter. The web-server subsequently responds with the requested timetables.</p>
<p>There are a total of 3 end-points in the web-server:</p>
<p><code>/generate</code> – Method that responds to a POST request, takes the given input and sends it to the LLM for timetable creation, once processed it responds with the timetable.</p>
<p><code>/save</code> – Method that responds to a POST request, takes JSON formatted timetable as an input and stores it in an external “timetable.json” file.</p>
<p><code>/get</code> – Method that responds to a GET request, sends all the saved timetables in a JSON format</p>
<h4>4.1.2. The Front-end</h4>
<p>The Front-end has been designed using HTML, CSS and JavaScript and compiled into an Electron App. The basic UI has been created using HTML and CSS, while JavaScript is used to make a POST request to the stated python web-server, by taking the input made in the UI to the web-server. After it has received the response, it creates a panel with the timetable on the screen. The user can then pass a judgement on whether it is the required timetable, and can save, or discard it.</p>
<p>If the user decides to save the table, it is stored on a JSON file in the back-end. Otherwise, the file is deleted permanently. The saved files can be accessed by the user anytime they wish.</p>
<h3>4.2. Security Control</h3>
<p>We use several systems to secure user data. HTTPS and TLS, file Backups and Real Time Monitoring.</p>
<ol>
  <li><b>HTTPS and TLS</b>: HTTPS (Hyper Text Transfer Protocol Secure) is used for all API communications. Our systems also use Transport Layer Security (TLS) to established secure connections. These protocols ensure data confidentiality and integrity during transmission</li>
  <li><b>File Backup</b>: It is as simple as it sounds. Each saved file is securely backed up so that if a malicious attack were to take place, the user would not loose their data</li>
  <li><b>Real Time Monitoring</b>: We have implemented several monitoring and logging tools, which will alert us if something goes wrong.</li>
</ol>
<h2>5. Conclusion</h2>
<p>In summary, the Time Table Creator (TTC) represents a significant advancement in personal productivity tools by harnessing the power of AI to streamline the often tedious process of timetable creation. By providing a user-friendly interface and intelligent scheduling capabilities. TTC empowers users to focus on their tasks rather than the mechanisms of planning. The application’s versatility makes it suitable for a wide range of users, from students to professionals, addressing common challenges faced in time management.</p>
<p>With robust security measures in place, including web application firewalls, file backups, and real-time monitoring. TTC ensures the safety and integrity of user data. As the application continues to evolve, future enhancements promise to deliver even greater precision and adaptability, paving the way for more sophisticated applications in various industries.</p>
<p>Ultimately, the TTC aims to reduce how users manage their time, promoting productivity and efficiency in an increasingly fast-paced world. By minimizing the effort required for planning, the TTC allows users to reclaim valuable time, enabling them to focus on what truly matters: their work and personal goals.</p>
<h2>6. References</h2>
<p>Flask. (2010-2024). Flask Documentation (Version 3.0.2). Pallets. <a href="https://flask.palletsprojects.com/ ">https://flask.palletsprojects.com/</a></p>
<p>Python Software Foundation. (2024). Python Documentation (Version 3.12). <a href="https://docs.python.org/3/">https://docs.python.org/3/</a></p>
<p>Groq. (2024). Groq LPU™ Documentation. <a href="https://docs.groq.com/">https://docs.groq.com/</a></p>
<p>Airbnb. (2015-2024). Lottie Documentation. <a href="https://airbnb.io/lottie/">https://airbnb.io/lottie/</a></p>
<p>Arctic Ice Studio & Sven Greb. (2016-2024). Nord Theme Documentation. <a href="https://www.nordtheme.com/docs/">https://www.nordtheme.com/docs/</a></p>
<p>Apple Inc. (2024). San Francisco UI Documentation. <a href="https://developer.apple.com/fonts/">https://developer.apple.com/fonts/</a></p>
<p>Electron. (2024). Electron Documentation. <a href="https://www.electronjs.org/docs">https://www.electronjs.org/docs</a></p>
