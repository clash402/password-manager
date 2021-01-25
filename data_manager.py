import json


class DataManager:

    # PUBLIC METHODS
    def save(self, website_input, username_input, password_input, messagebox):
        website = website_input.get()
        username = username_input.get()
        password = password_input.get()
        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

        if website == "" or username == "" or password == "":
            messagebox.showinfo(title="Error", message="Please fill in all entries")
        else:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            finally:
                messagebox.askokcancel(title="Title", message="New entry saved!")

    def find_website(self, website_input, messagebox):
        website = website_input.get()

        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No entry found")
        else:
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details fo {website} exist")
