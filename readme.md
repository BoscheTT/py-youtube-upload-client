# Guide to Obtain the `client_secret.json` for YouTube API Authentication

This guide will show you how to obtain the `client_secret.json` file needed to authenticate with the YouTube API and upload videos using Python.

## Steps to Obtain the `client_secret.json`

1. **Access the Google Cloud Console**:
   Go to the [Google Cloud Console](https://console.cloud.google.com/) and log in with your Google account. If you don't have an account, create one.

2. **Create a New Project**:
   - In the Google Cloud Console, click on **"Select a project"** at the top left, and then click on **"New Project"**.
   - Give your project a name and click **"Create"**.

3. **Enable the YouTube Data API**:
   - Go to the **API & Services** section in the left menu, then click on **Library**.
   - Search for **YouTube Data API v3** in the search bar.
   - Click on **YouTube Data API v3** and then click **Enable**.

4. **Create Credentials for Authentication**:
   - Go to the **Credentials** section under **API & Services** in the left menu.
   - Click **Create Credentials** and select **OAuth 2.0 Client ID**.
   - If prompted, set up the OAuth consent screen. You can add a name, icon, and a short description, then save it.
   - After configuring the consent screen, go back to the Credentials section and select **OAuth 2.0 Client ID**.
   - Choose **Desktop app** as the application type.
   - Name your credentials and click **Create**.
   - After creating the credentials, download the JSON file by clicking **Download**.

5. **Save the `client_secret.json` File**:
   - The downloaded file is your `client_secret.json`. Save it in the same folder as your Python script, or in a directory accessible by your script.

## How to Use the `client_secret.json`

1. Once you have obtained the `client_secret.json` file, place it in your project folder.
2. The Python script will automatically authenticate using this file when you run the command to upload the video.

## Example Usage

Once you have the `client_secret.json` file, you can use the Python code to upload videos to YouTube.

Run the command:

```bash
python upload_video.py video.mp4 "Video Title" "Video Description" --privacy unlisted
