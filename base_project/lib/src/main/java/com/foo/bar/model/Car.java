package com.foo.bar.model;

import com.foo.bar.api.ICar;

public class Car implements ICar
{
  public String type = "brum brum";

  @Override
  public String getType() {
    return type;
  }
}
