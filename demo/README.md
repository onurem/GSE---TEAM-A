# Hateless demo

The api let its users to analyze the content of a text message. Result returned consists of the api's classification label for the text. There are three labels:

- Label '0' - `Hate speech`
- Label '1' - `Offensive speech`
- Label '2' - `Neither`

## Changelogs

This section keeps track of changes in this documentation

| Date           | Author       | Description    |
| -------------- | ------------ | -------------- |
| June 6th, 2022 | Nguyen (Jim) | README created |

A demo for Hateless webservice—see [Online DEMO](https://hateless.herokuapp.com)

![Demo_Thumb](./images/demo_thumb.png)

## Specifications

### 0. Overview

```txt
./demo
|---- README       // Project structures, specs, etc.
|---- web_api      // Backend sub-project
|---- web_app      // Frontend sub-project
|---- docs         // Engineering documentations
```

Two main components for project:

- Backend API
- Frontend web application

**Note:**

- Frontend web app is built and delivered by backend api at root
- To run the demo on your local, please re-create virtual environment with dependency listed in `web_api/requirements.txt` then execute the `wsgi.py` with the venv's Python
- To run the frontend only, change directory to `web_app/hateless` then run `npm run start`

### 1. Backend

- **Flask 2.0.2**: WSGI web application frame work [BSD License]
- **Gunicorn 20.1.0**: Also WSGI framework, but supports workers feature extension to **Flask** sequential request processing model
- **Scikit-learn**: ML library to load picked models by ML team (I picked )
  
### 2. Frontend

- **ReactJS 11.7.1**: JavaScript library for Web UI
- **MUI 5.2**: A React component library following Google's **Material UI**

### 3. Deployment plan

- Platform: Heroku
- Contacts:
  - Nguyen (Jim) - [nguyenng178@gmail.com](nguyenng178@gmail.com)
- Website: [Hateless Heroku app](https://hateless.herokuapp.com/)