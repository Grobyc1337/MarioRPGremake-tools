# MarioRPGremake Modding Tools

These tools lets you add new spells for enemies in Mario RPG Remake
```
With these tools you can add new components (spells) in the following .json list :
1 - action.json
2 - battle_motion_monster.json
3 - menu_text_eng_us.json

How to use : 
eg. : Using the action.json -> drop your .json in the corresponding folder (action_tool folder in this example)

1 : run the "simplified.py" with "action.json" list to get a simplified action list which you can edit to add new components.

2 : run the "add_action_skill_tool.py" with your new "action_simplified.json" list to add your custom new skill(s).
    -> add the desired amount of new action(s)
3 : Once you get your final list "action_simplified_added.json"
    -> run "rebuild.py" with "action_simplified_added.json"  this will generate a new "action.json" in a new folder named output!
    Your new "action.json" is ready to be reserialize to .tbl for use. 
```
    * Will try to provide a short video on how to use the tools!
