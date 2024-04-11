def Settings(**kwargs):
    if kwargs['language'] == 'java':
        return {
            'ls': { 'settings': {
                'java.import.gradle.java.home': '/opt/homebrew/Cellar/openjdk@11/11.0.22'
            } }
        }
