instructions:

* Build stuff (optional)

```
cd base_project
./gradlew publishToMavenLocal
cd ../consumer_project
./gradlew build
```

* Open ./base_project/.ycm_extra_conf.py and change the java home to point
  at a valid installation of java 11 (or change languageVersion in
  **/build.gradle to some version you have installed)
* Open ./consumer_project/.ycm_extra_conf.py and change the java home to point
  at a valid installation of java 11 (or change languageVersion in
  **/build.gradle to some version you have installed)

* Open ./consumer_project/app/src/main/java/org/example/App.java
* Expect to be able to GoToDefinition from `Car` to `Car` in base_project
* Actual : Nope

* Open ./base_project/lib/src/main/java/com/foo/bar/model/Car.java
* Do a "GoToReferences" on `Car` (expect to see the refs in App.java from
  consumer_project)
* Actual : It's not recognised as a project file

* Open ./consumer_project/.ycm_extra_conf.py and uncomment the fancy jdt.ls
  folder stuff, repeat tests?
