# Python Flask User API

A simple Python Flask app exposing a POST endpoint to receive user data (`username`, `email`) in JSON format.

## 📦 How to Run Locally

### Prerequisites

- Python 3.7+
- pip

### Steps

```bash
pip install -r requirements.txt
python app.py
```

The app will start on `http://localhost:8080`.

Example `POST` request:

```bash
curl -X POST http://localhost:8080/api/users \
     -H "Content-Type: application/json" \
     -d '{"username":"johndoe","email":"john@example.com"}'
```

## ☸️ How to Deploy on OpenShift

1. **Build the Docker image:**

```bash
docker build -t your-registry/python-user-api .
```

2. **Push the image to your container registry:**

```bash
docker push your-registry/python-user-api
```

3. **Create OpenShift Deployment config:**

Save the following as `deployment.yaml` (replace image with your registry path):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-user-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-user-api
  template:
    metadata:
      labels:
        app: python-user-api
    spec:
      containers:
        - name: python-user-api
          image: your-registry/python-user-api
          ports:
            - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: python-user-api
spec:
  selector:
    app: python-user-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

4. **Deploy to OpenShift:**

```bash
oc apply -f deployment.yaml
```

5. **Expose the service (optional):**

```bash
oc expose svc/python-user-api
```

You can then access the app through the route created by OpenShift.

