package input

extension (resourceString: String)
  def resource: DataInput = Resource(resourceString)
  def file: DataInput = File(resourceString)
