pipeline {
    agent any
    environment {
        IMAGE_FLASK = "flask"
        IMAGE_NGINX = "nginx"
        CONTAINER_NAME = "container-pipeline"
        
    }
    stages {
      
        stage('Build') {
            steps {
                //  Building new image

                sh '/usr/local/bin/minikube start'
                sh 'eval $(/usr/local/bin/minikube docker-env)'
              
                sh '/usr/bin/docker image build -t $IMAGE_FLASK:1.0 -f flask/Dockerfile flask'
                sh '/usr/bin/docker image build -t $IMAGE_NGINX:1.0 -f nginx/Dockerfile nginx'
                
                echo "Images built and pushed to repository"
            }
        }
        stage('Deploy') {
            steps {
                script{
    
                   sh 'kubectl delete deployment backend frontend'
                   sh 'kubectl delete svc hello frontend'
                   sh 'kubectl apply -f flask.yaml'
                   sh 'kubectl apply -f nginx.yaml'
                   echo "Backend and frontend services are deployed"
                }
            }
        }
    }
}

