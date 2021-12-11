def callbackURL
pipeline {
  agent {
    label 'windows'
  }
  stages {
    stage('Setup parameters') {
      steps {
        script {
          properties([
            parameters([
              choice(
                choices: ['Node1', 'Node2'],
                name: 'Select Test Node'
              ),
              choice(
                choices: ['New Plan', 'Last Plan'],
                name: 'Execution Plan'
              ),
              string(
                defaultValue: 'scriptcrunch',
                name: 'Network Switch IP Address',
                trim: true
              ),
              choice(
                choices: ['harsh', 'prateek'],
                name: 'Select switch username'
              ),
              choice(
                choices: ['HG1', 'HG2'],
                name: 'Select switch hardware group'
              ),
              choice(
                choices: ['G1', 'G2'],
                name: 'Select Campaign'
              ),
              string(
                defaultValue: '0',
                name: 'Test Timeout (Minutes)',
                trim: true
              ),
              booleanParam(
                defaultValue: true,
                description: '',
                name: 'Hard Reboot Between Tests'
              ),
              choice(
                choices: ['NLA_5_1_0_REV01', 'NLA_6_1_0_REV01'],
                name: 'E500 Build Label'
              ),
              text(
                defaultValue: ''
                '
                this is a multi - line string parameter example ''
                ', 
                name: 'Additonal Stats Command'
              ),
            ])
          ])
        }
      }
    }
    stage('Pre Setup Checklist') {
      steps {
        script {
          echo 'echo s1'
          hook = registerWebhook()
          callbackURL = hook.getURL()
        }
      }
    }
    stage('Setup BTS') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Setup C2') {
      steps {
        bat 'echo s1'
      }
    }
    stage('run-parallel-branches') {
      steps {
        parallel(
          a: {
            echo "This is branch a"
          },
          b: {
            echo "This is branch b"
          }
        )
      }
    }
    stage('Reboot EM500') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Start RTC') {
      steps {
        bat 'echo s1'
      }
    }
    stage('RTC Health Check') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Start BTS Service') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Start Core Network Service') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Save Results to Graphite') {
      steps {
        bat 'echo s1'
      }
    }
    stage('Wait on Webhook') {
      options {
        timeout(time: 60, unit: "MINUTES")
      }
      steps {
        parallel(
          a: {
            script {
              echo "Waiting for POST to ${callbackURL}"
              data = waitForWebhook hook
              echo "Webhook called with data: ${data}"
              //def jsonObj = readJSON text: data
              //echo $ {
              // jsonObj.status
              //}
            }
          },
          b: {
            bat "python scheduler.py ${callbackURL}"
          }
        )
      }
    }
    //     stage('reports') {
    //     steps {
    //     script {
    //             allure([
    //                     includeProperties: false,
    //                     jdk: '',
    //                     properties: [],
    //                     reportBuildPolicy: 'ALWAYS',
    //                     results: [[path: 'target/allure-results']]
    //             ])
    //     }
    //     }
    // }
    stage("Plot Results") {
      steps {
        plot csvFileName: 'plot-5c43d682-6222-4316-bda9-ba661f8780bd.csv', csvSeries: [
          [displayTableFlag: true, exclusionValues: '', file: 'results.csv', inclusionFlag: 'OFF', url: '']
        ], group: 'TMA', numBuilds: '3', style: 'line', title: 'TMA Testplan Results', useDescr: true, yaxis: 'Y Axis Data'
      }
    }
  }
}