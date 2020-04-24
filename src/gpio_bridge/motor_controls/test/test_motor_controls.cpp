#include "motor_controls/motor_controls.hpp"

#include <chrono>
#include <iostream>
#include <rclcpp/rclcpp.hpp>

using namespace std::chrono_literals;

auto main() -> int
{
   const auto& logger = rclcpp::get_logger("test_motor_controls");
   auto& controller = motor_controls::MotorController::get();

   constexpr uint8_t DUTY_CYCLE = 100;

   RCLCPP_INFO(logger, "Actuating motors forward for 10 seconds at 100%% duty cycle");
   motor_controls::Command command{motor_controls::Direction::FORWARD, DUTY_CYCLE, 10s};
   controller.actuate(command);

   RCLCPP_INFO(logger, "Actuating motors reverse for 10 seconds at 100% duty cycle");
   command.direction = motor_controls::Direction::REVERSE;
   controller.actuate(command);
}
