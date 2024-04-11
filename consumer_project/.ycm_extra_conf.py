import os

DIR_OF_THIS_SCRIPT = os.path.abspath( os.path.dirname( __file__ ) )

def Abs( *args ):
  return os.path.abspath( os.path.join( DIR_OF_THIS_SCRIPT, *args ) )

def Uri( *args ):
  return 'file://' + Abs( *args )

def Settings(**kwargs):
  if kwargs['language'] == 'java':
    return {
      'ls': { 
        'settings': {
          'java.import.gradle.java.home': '/opt/homebrew/Cellar/openjdk@11/11.0.22'
        },
        # Uncomment to use the jdt.ls wierd version of workspaceFolders
        #
        # 'workspaceFolders': [
        #   Uri( DIR_OF_THIS_SCRIPT ),
        #   Uri( '..', 'base_project' ),
        # ]
      },
      'additional_workspace_dirs': [
        Abs( '..', 'base_project' ),
      ]
    }
