pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    ansiColor('vga')
  }
  triggers {
    pollSCM 'H/15 * * * *'
    cron 'H H * * *'
  }
  stages {
    stage ("Build Environment") {
      steps {
        sh '''
          source /usr/local/bin/activate
          python -V
          ansible --version
          molecule --version
        '''
      }
    }
    stage ("Syntax") {
      steps {
        sh '(source /usr/local/bin/activate && molecule syntax)'
      }
    }
    stage ("Linting") {
      steps {
        sh '(source /usr/local/bin/activate && molecule lint)'
      }
    }
    stage ("Playbook") {
      steps {
        sh '(source /usr/local/bin/activate && molecule converge)'

      }
    }
    stage ("Verification") {
      steps {
        sh '(source /usr/local/bin/activate && molecule verify)'
      }
    }
    stage ("Idempotency") {
      steps {
        sh '(source /usr/local/bin/activate && molecule idempotence)'
      }
    }
  }
}
