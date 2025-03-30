import os
import argparse
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from tqdm import tqdm  # Importa tqdm per la barra di progresso

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def upload_video_with_progress(youtube, file, title, description, category="22", privacy="public"):
    # Ottieni la dimensione del file
    file_size = os.path.getsize(file)  # in byte
    file_size_mb = file_size / (1024 * 1024)  # in MB
    
    chunk_size = 1 * 1024 * 1024  # 10 MB
    media = googleapiclient.http.MediaFileUpload(file, chunksize=chunk_size, resumable=True)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["Python", "YouTube API"],
                "categoryId": category,  # 22 = "People & Blogs"
            },
            "status": {
                "privacyStatus": privacy  # public, private, unlisted
            },
        },
        media_body=media
    )
    
    # Variabili per il monitoraggio del progresso
    response = None
    progress_bar = tqdm(total=file_size_mb, unit="MB", desc="Uploading video")  # Barra di progresso

    while response is None:
        # Carica il video e monitora il progresso
        status, response = request.next_chunk()
        
        if status:
            # Calcola i MB caricati
            uploaded_mb = status.resumable_progress / (1024 * 1024)  # Converti in MB
            remaining_mb = file_size_mb - uploaded_mb  # Calcola i MB rimanenti
            
            # Aggiorna la progress bar
            progress_bar.update(uploaded_mb - progress_bar.n)  # Aggiungi la quantità caricata alla barra
            progress_bar.set_postfix({"Uploaded": f"{uploaded_mb:.2f} MB", "Remaining": f"{remaining_mb:.2f} MB"})
    
    progress_bar.close()  # Chiudi la barra di progresso quando l'upload è completato
    print(f"Video uploaded! ID: {response['id']}")
    return response['id']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a video to YouTube")
    parser.add_argument("file", help="Path to the video file")
    parser.add_argument("title", help="Title of the video")
    parser.add_argument("description", help="Description of the video")
    parser.add_argument("--category", default="22", help="Category ID (default: 22 - People & Blogs)")
    parser.add_argument("--privacy", default="public", choices=["public", "private", "unlisted"], help="Privacy status")

    args = parser.parse_args()

    youtube = authenticate()
    upload_video_with_progress(youtube, args.file, args.title, args.description, args.category, args.privacy)
