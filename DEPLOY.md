# Deployment notes (Cloud Run guide - optional)

1. Build container: docker build -t gcr.io/<PROJECT>/smartsupport:latest .
2. Push: docker push gcr.io/<PROJECT>/smartsupport:latest
3. Deploy to Cloud Run: gcloud run deploy smartsupport --image gcr.io/<PROJECT>/smartsupport:latest --platform managed --region us-central1
4. Secure with IAM as required.
