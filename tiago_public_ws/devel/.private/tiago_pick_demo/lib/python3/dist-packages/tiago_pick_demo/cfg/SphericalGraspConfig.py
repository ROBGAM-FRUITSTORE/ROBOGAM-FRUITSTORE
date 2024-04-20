## *********************************************************
##
## File autogenerated for the spherical_grasps_server package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'grasp_postures_frame_id', 'type': 'str', 'default': 'arm_tool_link', 'level': 0, 'description': 'pre_grasp_posture and grasp_posture frame_id, usually the tool (previous to the gripper)', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'gripper_joint_names', 'type': 'str', 'default': 'gripper_left_finger_joint gripper_right_finger_joint', 'level': 0, 'description': 'gripper joint names', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'gripper_pre_grasp_positions', 'type': 'str', 'default': '0.05 0.05', 'level': 0, 'description': 'gripper pre_grasp joint positions (same order than joint_names)', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'gripper_grasp_positions', 'type': 'str', 'default': '0.01 0.01', 'level': 0, 'description': 'gripper pre_grasp joint positions (same order than joint_names)', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'time_pre_grasp_posture', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Time for the pre_grasp gripper posture to be achieved', 'min': 0.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'time_grasp_posture', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Time for the grasp gripper posture to be achieved (will be added to pre_grasp_posture)', 'min': 0.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'time_grasp_posture_final', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Time for the grasp gripper final posture to be achieved (will be added to time_grasp_posture)', 'min': 0.0, 'max': 10.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'grasp_pose_frame_id', 'type': 'str', 'default': 'base_footprint', 'level': 0, 'description': "grasp pose frame id is the frame where the object pose is expressed. Pose must be in the frame of MoveIt's base frame, base_footprint usually", 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'grasp_desired_distance', 'type': 'double', 'default': 0.15, 'level': 0, 'description': 'grasp desired distance for pre grasp, post grasp and place', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'grasp_min_distance', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'grasp min distance for pre grasp, post grasp and place', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pre_grasp_direction_x', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Pre grasp approach x direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pre_grasp_direction_y', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Pre grasp approach y direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pre_grasp_direction_z', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Pre grasp approach z direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'post_grasp_direction_x', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'Post grasp retreat x direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'post_grasp_direction_y', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Post grasp retreat y direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'post_grasp_direction_z', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Post grasp retreat z direction vector', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'grasp_quality', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'grasp quality to set to the grasp', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_contact_force', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'max_contact_force', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'allowed_touch_objects', 'type': 'str', 'default': '', 'level': 0, 'description': 'allowed_touch_objects', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'fix_tool_frame_to_grasping_frame_roll', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Fix the transformation of the tool_link frame to the grasping_frame roll (degrees)', 'min': -360.0, 'max': 360.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'fix_tool_frame_to_grasping_frame_pitch', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Fix the transformation of the tool_link frame to the grasping_frame pitch (degrees)', 'min': -360.0, 'max': 360.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'fix_tool_frame_to_grasping_frame_yaw', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Fix the transformation of the tool_link frame to the grasping_frame yaw (degrees)', 'min': -360.0, 'max': 360.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'step_degrees_yaw', 'type': 'int', 'default': 10, 'level': 0, 'description': 'Degrees step over yaw on generating the grasp poses', 'min': 1, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'step_degrees_pitch', 'type': 'int', 'default': 10, 'level': 0, 'description': 'Degrees step over pitch on generating the grasp poses', 'min': 1, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'min_degrees_yaw', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Starting degrees over yaw on generating grasp poses', 'min': 0, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'max_degrees_yaw', 'type': 'int', 'default': 360, 'level': 0, 'description': 'Stopping degrees over yaw on generating grasp poses', 'min': 0, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'min_degrees_pitch', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Starting degrees over pitch on generating grasp poses', 'min': 0, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'max_degrees_pitch', 'type': 'int', 'default': 360, 'level': 0, 'description': 'Stopping degrees over pitch on generating grasp poses', 'min': 0, 'max': 360, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

