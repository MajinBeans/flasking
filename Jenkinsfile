pipeline {
  agent {
    node {
      label 'docker'
    }

  }
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/MajinBeans/flasking.git', branch: 'main')
      }
    }

    stage('Docker Build') {
      steps {
        sh 'docker build -t majindean/flask_app .'
      }
    }

    stage('Docker Login') {
      steps {
        sh 'docker login -u majindean -p dckr_pat_GTakJpJREGg5L9T5HjBdEKiOJmY'
      }
    }

    stage('Docker Push') {
      steps {
        sh 'docker push majindean/flask_app'
      }
    }

  }
}