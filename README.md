# Tech Sentinel

**Tech Sentinel** is an open-source AI Agent designed for developers and project managers.  
It automatically tracks, summarizes, and notifies GitHub repository updates on a daily or weekly basis, helping teams stay synced, quickly respond to changes, and boost collaboration efficiency.

## ✨ Features

- **Subscription Management**: Subscribe to your favorite GitHub repositories.
- **Automated Fetching**: Regularly fetch commits, pull requests, and issues.
- **Smart Notification System**: Deliver updates via email, Slack, or other channels.
- **Report Generation**: Summarize updates into daily/weekly reports.
- **Customizable Schedule**: Configure update intervals and notification channels.
- **Modular Architecture**: Easy to extend and customize.

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/tech_sentinel.git
   cd tech_sentinel
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up environment variables or modify `config.py` for your GitHub token and preferences.

---

## 🚀 Usage

1. Add repositories you want to track into `subscriptions.json`:

   ```json
   [
     "https://github.com/example/repo1",
     "https://github.com/example/repo2"
   ]
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. The system will:
   - Periodically fetch updates
   - Generate a summary report
   - Send notifications

---

## ⚙️ Configuration

Edit the `config.py` file to adjust:

- `GITHUB_TOKEN`: Your GitHub personal access token (required for higher API limits).
- `SUBSCRIPTION_FILE`: The JSON file storing your repository subscriptions.
- `SCHEDULE_INTERVAL`: Choose `daily` or `weekly`.
- `NOTIFICATION_CHANNELS`: Choose one or more from `["email", "slack", "dingtalk"]`.

---

## 🤝 Contributing

Contributions are welcome!  
Here's how you can help:

- **Report bugs** via [Issues](https://github.com/your-username/tech_sentinel/issues)
- **Suggest features** or improvements
- **Submit pull requests** to add new notifiers, support new GitHub events, or enhance report formats

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details (to be created).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

Project maintained by **[Your Name or Organization]**.  
Feel free to reach out via GitHub Issues or [email@example.com](mailto:email@example.com).

---