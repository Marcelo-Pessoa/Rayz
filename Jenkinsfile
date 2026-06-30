pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando o processo de Build...'
                script {
                    // Fazendo pull da imagem de build
                    bat 'docker pull node:16-alpine'
                    
                    // execução do build adaptando ao ambiente nativo windows do Docker
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        node:16-alpine \
                        sh -c "echo 'Instalando dependências e buildando...' && npm install"
                    '''
                }
            }
        }

        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados em um container separado...'
                script {
                    // Fazendo pull de imagem com compatibilidade com Python e Node
                    bat 'docker pull nikolaik/python-nodejs:python3.10-nodejs16-alpine'
                    
                    // Executando os testes unitarios
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        nikolaik/python-nodejs:python3.10-nodejs16-alpine \
                        sh -c "python testes_main.py -v"
                    '''
                }
            }
        }
    }
}