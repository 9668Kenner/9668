# TODO: insert robot code here
import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.leftbackDrive = wpilib.PWMSparkMax(4)
        self.leftfrontDrive = wpilib.PWMSparkMax(7)
        self.rightfrontDrive = wpilib.PWMSparkMax(2)
        self.rightbackDrive = wpilib.PWMSparkMax(6)
        self.launcherback = wpilib.PWMSparkMax(8)
        self.launcherfront = wpilib.PWMSparkMax(9)
        self.leftbackDrive = wpilib.PWMSparkMax(1)
        self.leftDrive = self.leftbackDrive,self.leftfrontDrive
        self.rightdrive = self.rightbackDrive,self.rightfrontDrive
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftDrive, self.rightdrive
        )
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        self.rightDrive.setInverted(True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()  # Stop robot

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getRightX()
        )


if __name__ == "__main__":
    wpilib.run(MyRobot)