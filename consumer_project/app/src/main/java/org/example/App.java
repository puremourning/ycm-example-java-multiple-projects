/*
 * This source file was generated by the Gradle 'init' task
 */
package org.example;

import com.foo.bar.api.ICar;
import com.foo.bar.model.Car;

public class App {
    public String getGreeting() {
        ICar car = new Car();
        return car.getType();
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
