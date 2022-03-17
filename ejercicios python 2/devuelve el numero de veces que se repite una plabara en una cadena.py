def upload_count(dates, month):
  return  len([x for x in dates if month in x])









print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept"))
