pipeline {
    agent any // Tells Jenkins to use the Windows agent natively first

    stages {
        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados dentro do container...'
                
                // We use script block to explicitly run the container with correct Linux pathing
                script {
                    // Pull the image manually to be safe
                    bat 'docker pull node:16-alpine'
                    
                    // Run the container via an explicit bat command
                    // We map the workspace to /workspace and override the working directory properly
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        node:16-alpine \
                        sh -c "echo 'Node version: ' && node -v && python testes_main.py -v"
                    '''
                }
            }
        }
    }
}
//set "PATH=C:\\Users\\Lucas Rangel\\AppData\\Local\\Programs\\Python\\Python312;%PATH%"