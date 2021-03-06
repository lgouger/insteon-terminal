#-------------------------------------------------------------------------------
#
# Base class for all dimmers
#
import iofun
import message
from querier import MsgHandler

from us.pfrommer.insteon.msg import InsteonAddress
from light import Light

class Dimmer(Light):
	def __init__(self, name, adr):
		Light.__init__(self, name, adr)
	def onFast(self, level=0xFF):
		"""onFast(level)
		switch light on fast, to given level"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x12, level, -1))

	def offFast(self):
		"""offFast()
		switch light off fast"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x14, 0x00, -1))

        def setButtonOnLevel(self, level=0xFF, button=0x01):
		"""setButtonOnLevel(level=0xFF, button=0x01)
		sets the on level for a button to the specified level (between 0x00 and 0xFF) """
		self.querier.setMsgHandler(MsgHandler("set button on level"))
		self.querier.queryext(0x2E, 0x00, [button, 0x06, level])

        def setButtonRampRate(self, rate=0x1f, button=0x01):
		"""setButtonRampRate(rate=0x1F, button=0x01)
		sets the on level for a button to the specified level (between 0x00 and 0xFF) """
		self.querier.setMsgHandler(MsgHandler("set button ramp rate"))
		self.querier.queryext(0x2E, 0x00, [button, 0x05, rate])

	def incrementalBright(self):
		"""incrementalBright()
		brighten light incrementally"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x15, 0x00, -1))

	def incrementalDim(self):
		"""incrementalDim()
		dim light incrementally"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x16, 0x00, -1))

	def startManualChangeUp(self):
		"""startManualChangeUp()
		start manual change, dim up"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x17, 0x01, -1))

	def startManualChangeDown(self):
		"""startManualChangeDown()
		start manual change, dim down"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x17, 0x00, -1))

	def stopManualChange(self):
		"""stopManualChange()
		stop manual change"""
		iofun.writeMsg(message.createStdMsg(
			InsteonAddress(self.getAddress()), 0x0F, 0x18, 0x00, -1))

