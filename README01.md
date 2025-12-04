flowchart LR
  A[Code (local)] --> B[GitHub Repository]
  B --> C[GitHub Actions Workflow]
  C --> D[Run tests + Cache deps]
  D -->|Success| E[Build Docker image]
  E --> F[Push to Docker Hub]
  F --> G[Deploy]
