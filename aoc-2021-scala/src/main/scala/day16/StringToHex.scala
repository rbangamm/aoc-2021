package day16

extension (s: String)
  def hexToBinary: String = BigInt(s, 16).toString(2)
  def binaryToDecimal: Int = Integer.parseInt(s,  2)