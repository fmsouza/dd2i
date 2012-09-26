class Trigger:
	def shoot(self):
		self.triggerCallback()

	def condition(self):
		return False

	def wait(self):
		if self.condition():
			self.shoot()

