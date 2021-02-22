# import threading
import sqlite3
import os.path
import datetime
from vector.apps.RGWUtility import rgw_data
# from RGWUtility import rgw_data

class RepositoryDB:
  def __init__(self, sqlite_file):
    self.repo_helper = rgw_data.RepoDataHelper(sqlite_file)

  def get_profile_id_on_name(self, name):
    return self.repo_helper.get_profile_id_on_name(name)

  def set_setting(self, profileID, profileDataKey, profileDataValue):
    self.repo_helper.set_setting(profileID, profileDataKey, profileDataValue)
    
  def get_settings(self, profile_name):
    return self.repo_helper.get_settings(profile_name)

  def set_tc_data(self, tcUniqueID, tcDataType, tcDataValue):
    return self.repo_helper.set_tc_data(tcUniqueID, tcDataType, tcDataValue)

  def get_tc_data(self, tc_unique_id):
    tc_detail = self.repo_helper.get_testcase_detail_on_unique_id(tc_unique_id)
    tc_id = tc_detail[0]

    tc_data_consolidated = {}
    tc_data_consolidated["environment"] = tc_detail[1]
    tc_data_consolidated["unit_name"] = tc_detail[2]
    tc_data_consolidated["subprogram_name"] = tc_detail[3]
    tc_data_consolidated["tc_name"] = tc_detail[4]
    
    tc_data = self.repo_helper.get_testcase_data_latest_all(tc_id)
    for tc_data_row in tc_data:
      tc_data_consolidated[tc_data_row[3]] = tc_data_row[4]
      if tc_data_row[2] == 7: tc_data_consolidated["dts"] = tc_data_row[5]
    return tc_data_consolidated

  def get_req_last_updated_dts(self, req_key):
    return self.repo_helper.get_requirement_tracking_max_date_on_key(req_key)
