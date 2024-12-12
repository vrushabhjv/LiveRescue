# LiveRescue

LiveRescue is an innovative real-time chat application built to address critical situations by facilitating seamless communication between victims and volunteers. The platform is designed to provide a lifeline in emergencies, offering users the ability to create and join chat rooms dedicated to specific incidents or causes. By integrating WebSocket technology and persistent message storage, LiveRescue ensures that no crucial detail is missed during coordination efforts. Additionally, volunteers can register to provide assistance, bridging the gap between those in need and those ready to help.

## Features

- **Real-Time Communication**: Leverages WebSocket technology through Django Channels to enable instant messaging without delays.
- **Dynamic Chat Rooms**: Users can create specialized chat rooms for focused discussions or join existing ones to contribute to ongoing conversations.
- **Persistent Message History**: All messages are stored and accessible, ensuring that users can review past interactions and important details.
- **Volunteer Registration**: Dedicated functionality for users to sign up as volunteers, fostering a supportive community to assist in emergencies.
- **Secure User Authentication**: A robust login and registration system ensures that only authorized users can access the platform.
- **Scalable Architecture**: Built with scalability in mind to handle increasing user traffic and real-time data flow efficiently.

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: TailwindCSS
- **Backend**: Python, Django with Django Channels (WebSocket support)
- **Database**: SQLite (for development), can be configured to use PostgreSQL or MySQL for production.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Vrushabhjv/LiveRescue.git
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate # For Linux/macOS
   env\Scripts\activate   # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and run the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open the application in your browser at `http://127.0.0.1:8000`.

## Contact

For any queries or suggestions, feel free to reach out:

- **Name**: Vrushabh J V
- **GitHub**: [github.com/vrushabhjv](https://github.com/vrushabhjv)

---
