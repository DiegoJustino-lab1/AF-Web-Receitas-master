# receitas-vuetify

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```





# Setting Up Django Project

## Step 1: Create a Virtual Environment

Navigate to the backend directory and run the following command:

```bash
python3 -m venv venv
```

## Step 2: Activate Virtual Environment

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

You should see (venv) appear at the beginning of your command prompt, indicating that the virtual environment is active.

## Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

## Step 4: Make the Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Step 5: Run the Server

```bash
python manage.py runserver
```

By default, the server will run on <http://127.0.0.1:8000/>.

## Step 6: Deactivate Virtual Environment

```bash
deactivate
```
