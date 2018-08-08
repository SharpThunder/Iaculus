#!groovy

node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            
                           
            
        stage 'Deploy'
	    find . -name "*.sh" -exec chmod +x {} \;

            sh './deploy_prod.sh'

        
        
    }

    catch (err) {
        
        throw err
    }

}
