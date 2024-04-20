## *********************************************************
##
## File autogenerated for the tiago_pcl_tutorial package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'setLeafSize_X', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'A double parameter', 'min': 0.0, 'max': 0.1, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'setLeafSize_Y', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'A double parameter', 'min': 0.0, 'max': 0.1, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'setLeafSize_Z', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'A double parameter', 'min': 0.0, 'max': 0.1, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Distance_Threshold', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'A double parameter', 'min': 0.0, 'max': 8.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Radius_Limit', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'A double parameter', 'min': 0.0, 'max': 8.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Optimize_Coefficients', 'type': 'bool', 'default': True, 'level': 0, 'description': 'A bool parameter', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'image', 'type': 'int', 'default': 1, 'level': 0, 'description': 'A PointCloud2 origin param which is edited via an enum', 'min': 0, 'max': 3, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'original_image', 'type': 'int', 'value': 0, 'srcline': 15, 'srcfile': '/home/mgs09/tiago_public_ws/src/tiago_tutorials/tiago_pcl_tutorial/cfg/segment.cfg', 'description': 'original image', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'filtered_image', 'type': 'int', 'value': 1, 'srcline': 16, 'srcfile': '/home/mgs09/tiago_public_ws/src/tiago_tutorials/tiago_pcl_tutorial/cfg/segment.cfg', 'description': 'filtered image', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to choose origin PointCloud2'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'method', 'type': 'int', 'default': 1, 'level': 0, 'description': 'A PointCloud2 origin param which is edited via an enum', 'min': 0, 'max': 3, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Plane', 'type': 'int', 'value': 0, 'srcline': 20, 'srcfile': '/home/mgs09/tiago_public_ws/src/tiago_tutorials/tiago_pcl_tutorial/cfg/segment.cfg', 'description': 'Plane', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Cylindrical', 'type': 'int', 'value': 1, 'srcline': 21, 'srcfile': '/home/mgs09/tiago_public_ws/src/tiago_tutorials/tiago_pcl_tutorial/cfg/segment.cfg', 'description': 'Cylindrical', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'Euclidean', 'type': 'int', 'value': 2, 'srcline': 22, 'srcfile': '/home/mgs09/tiago_public_ws/src/tiago_tutorials/tiago_pcl_tutorial/cfg/segment.cfg', 'description': 'Euclidean', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'An enum to choose method'}", 'ctype': 'int', 'cconsttype': 'const int'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

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

segment_original_image = 0
segment_filtered_image = 1
segment_Plane = 0
segment_Cylindrical = 1
segment_Euclidean = 2
