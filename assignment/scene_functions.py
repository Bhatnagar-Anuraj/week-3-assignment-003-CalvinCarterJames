"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so
       they can be reused at different locations and scales.
    4. Every function must return the name(s) of the Maya object(s) it creates.
    5. Follow PEP 8 naming conventions (snake_case for functions/variables).

GRADING CRITERIA:
    - [30%] At least 5 functions, each creating a distinct scene element.
    - [25%] Functions accept parameters and use them (not hard-coded values).
    - [20%] Every function has a complete docstring (summary, Args, Returns).
    - [15%] Functions return the created object name(s).
    - [10%] Clean, readable code following PEP 8.
"""

import maya.cmds as cmds
import math

def create_building(width=3.0, height=5.0, depth=5.0, position=(0,0,0)):
    """Create a simple building from a cube, placed on the ground plane."""
    building = cmds.polyCube(width = width, height = height, depth = depth)
    cmds.move(x, height/2.0, z, building)
    return building
"""returns the building variable"""
"""
    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
   
    


def create_tree( height=5.0, position = (0,0,0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy."""
    trunk = cmds.polyCylinder(radius = .3, height = height / 2.0)
    cmds.move(x, height / 2.0, z, trunk)
    leaves = cmds.polySphere(radius = 1,)
    cmds.move(x, height + 3, z, leaves)
    treegrp = cmds.group(leaves, trunk, name = "tree_grp")
    return treegrp
"""Returns: the trunk and leaves variable"""
"""
    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
   
    



def create_fencepost(x, z, height=2, width=0.6, depth=0.6):
    """creates the posts for the fence"""
    post = cmds.polyCube(height=height, width=width, depth=depth)
    cmds.move(x, height / 2, z)
    return post

def create_rail(length, y_height, position=(0, 0, 0), thickness=0.6, depth=0.2):
    """ creates the rail for the fence"""
    rail = cmds.polyCube(width=length, height=thickness, depth=depth)
    
    
    x = position[0] + length / 2
    y = y_height
    z = position[2]
    
    cmds.move(x, y, z)
    return rail

def create_fence(create_func, length=10, height=2, post_count=6, position=(0, 0, 0)):
    """places the rail and posts so they make a fence"""
    spacing = length / (post_count - 1)
    results = []
    for i in range(post_count):
        x = position[0] + i * spacing
        z = position[2]
        result = create_func(x, z, height=height)
        results.append(result)
        create_rail(length=length, y_height=height * 0.6, position=position)

    return results
    """returns the resulting fence variable"""
        
    """Create a simple fence made of posts and rails."""
    
    

"""
   The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
"""
   



def create_lamp(pole_height=5, light_radius=0.5, position = (0,0,0)):
    """Create a street lamp using a cylinder pole and a sphere light."""
    lamp_post = cmds.polycylinder(height = pole_height, radius = light_radius/2.0)
    cmds.move(x, pole_height/2, z, lamp_post)
    light = cmds.polySphere(radius = light_radius)
    cmds.move(x, pole_height + 4, z, light)
    lampgrp = cmds.group(lamp_post, light, name="lamp_grp")
    return lampgrp
    
    """
    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
   


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0), **kwargs):
    results = []
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = center[0] + radius * math.cos(angle)
        z = center[2] + radius * math.sin(angle)
        obj = create_func(position=(x, center[1], z), **kwargs)
        results.append(obj)

    return results
"""Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
