pipeline {
    agent {
        docker { 
            image 'node:16-alpine' 
            // 1. We map the Windows path to a Linux mount point inside the container
            args '-v /c/ProgramData/Jenkins/.jenkins/workspace/Docker/:/workspace'
        }
    }
    
    // 2. We force Jenkins to treat the workspace as the Linux path inside the container
    options {
        skipDefaultCheckout()
    }
    
    stages {
        stage('Testes Unitários') {
            // 3. We use a customWorkspace with a Linux-style path format for the steps
            agent {
                docker {
                    image 'node:16-alpine'
                    customWorkspace '/workspace'
                }
            }
            steps {
                // Manually checkout since we skipped the default one to avoid the path bug
                checkout scm 
                
                echo 'Executando os testes integrados do repositório...'
                sh '''
                    python testes_main.py -v
                '''
            }
        }
    }
}
//set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"