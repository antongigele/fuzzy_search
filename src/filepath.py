from sys import platform

remote_linux_path = "/home/anton/projects/data_source/"
remote_linux_append_path = "/home/anton/projects/anton-concept-node/util/"
remote_linux_output_path = "/home/anton/projects/anton-concept-node/clusters/"
remote_analytics_path = "/home/anton/projects/anton-concept-node/analytics/results/"
remote_data_source_path = "/home/anton/projects/anton-concept-node/fuzzy_search/data_source/"

local_mac_path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/csv_imports/"
local_mac_append_path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/util/"
local_mac_output_path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/clusters/"
local_analytics_path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/analytics/results/"
local_data_source_path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/fuzzy_search/data_source/"

if platform == "linux" or platform == "linux2":
    path = remote_linux_path
    append_path = remote_linux_append_path
    output_path = remote_linux_output_path
    analytics_path = remote_analytics_path
    data_source_path = remote_data_source_path
elif platform == "darwin":
    path = local_mac_path
    append_path = local_mac_append_path
    output_path = local_mac_output_path
    analytics_path = local_analytics_path
    data_source_path = local_data_source_path
else:
    path = local_mac_path
    append_path = local_mac_append_path
    output_path = local_mac_output_path
    analytics_path = local_analytics_path
    data_source_path = local_data_source_path