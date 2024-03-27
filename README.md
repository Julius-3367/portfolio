# GuestGuru

Streamlining visitor management with a user-friendly record-keeping system.

## Team

### Team Members:

- Julius Korir (Backend Developer)
- Christine Mwaniki (Frontend Developer)

### Roles:

- Julius Korir will be responsible for developing the backend API using Flask, handling data storage and retrieval, and ensuring secure user authentication.
- Christine Mwaniki will design and develop the user interface using React, focusing on creating a user-friendly and responsive experience for both receptionists and visitors.

## Rationale

These roles were chosen based on each team member's expertise and career aspirations. Julius, with his backend development experience, can efficiently manage data and security aspects. Christine, wanting to specialize in React, can leverage this project to gain practical experience with front-end development utilizing this framework.

## Technologies

### Languages:

- Python (backend)
- Javascript (frontend)

### Frameworks:

- Flask (backend)
- React (frontend)

### Additional Technologies:

- HTML
- CSS
- PostgreSQL (database)
- Git version control system

### Technology Trade-offs:

#### Backend: Flask vs Django

Both are popular Python frameworks. While Django offers more built-in functionalities, Flask was chosen for its lighter weight and greater flexibility, as this project is likely to have simpler backend requirements.

#### Frontend: React vs Angular

Both are popular Javascript frameworks. React was chosen due to its flexibility and growing popularity, particularly for its component-based architecture and compatibility with Christine's career aspirations.

## Challenge

### Problem:

The current manual visitor record-keeping process is inefficient, prone to errors, and lacks features for data analysis or reporting.

### Limitations:

This project focuses on visitor record-keeping. It won't handle complex visitor management features like scheduling appointments or integrating with access control systems.

### Target Users:

This project will benefit both receptionists and visitors. Receptionists will have a user-friendly system to manage visitor data, and visitors will experience a streamlined registration process.

### Locale Relevance:

While the system is not specific to a location, it can be customized to comply with any regional regulations regarding visitor information collection.

## Risks

### Technical Risks:

- Integration challenges: Ensuring smooth communication between the frontend and backend components.
- Database security vulnerabilities: Implementing appropriate security measures to protect sensitive visitor information.

### Safeguards:

- Utilize established libraries and best practices for secure communication and data handling.
- Conduct thorough testing to identify and address potential vulnerabilities.

### Non-Technical Risks:

- Scope creep: Project goals expanding beyond the initial plan, impacting development time and resources.
- Communication breakdown: Ineffective communication between team members leading to delays or misunderstandings.

### Strategies:

- Clearly define project scope and prioritize functionalities to manage expectations.
- Establish regular communication channels and maintain project documentation.

## Infrastructure

- Version Control: Utilize Git version control with a branching strategy like Git flow to manage code versions and facilitate collaboration.
- Deployment: Employ a cloud-based platform like Heroku for easy deployment and maintenance of the application.
- Data Population: Initially populate the system with sample data for testing purposes. Later, users can create and manage the data directly through the system's interface.
- Testing: Leverage automated testing tools like Jest for unit testing and Selenium for integration testing to ensure code functionality and application stability.

## Existing Solutions

Similar solutions include:

- Sign-in kiosks: Offer visitor self-registration, but lack personal interaction and data management features.
- Online visitor management software: Often complex and expensive, especially for smaller organizations.

This project aims to provide a user-friendly, cost-effective solution specifically designed for organizations with simpler visitor management needs. It will combine the ease of self-registration with the personalized experience and data management capabilities often missing in existing alternatives.

By addressing the limitations of existing solutions and catering to the specific needs of smaller organizations, this visitor record-keeping system has the potential to streamline visitor management processes and enhance the overall experience for both visitors and receptionists.

