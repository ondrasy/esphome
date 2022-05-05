from esphome import pins
from esphome.components import stepper
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_DIR_PIN, CONF_ID, CONF_SLEEP_PIN, CONF_STEP_PIN

CONF_STEP_PIN_2 = "step_pin_2"

a4988_dual_ns = cg.esphome_ns.namespace("a4988_dual")
A4988Dual = a4988_dual_ns.class_("A4988Dual", stepper.Stepper, cg.Component)

CONFIG_SCHEMA = stepper.STEPPER_SCHEMA.extend(
    {
        cv.Required(CONF_ID): cv.declare_id(A4988Dual),
        cv.Required(CONF_STEP_PIN): pins.gpio_output_pin_schema,
        cv.Required(CONF_STEP_PIN_2): pins.gpio_output_pin_schema,
        cv.Required(CONF_DIR_PIN): pins.gpio_output_pin_schema,
        cv.Optional(CONF_SLEEP_PIN): pins.gpio_output_pin_schema,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await stepper.register_stepper(var, config)

    step_pin = await cg.gpio_pin_expression(config[CONF_STEP_PIN])
    cg.add(var.set_step_pin(step_pin))
    step_pin_2 = await cg.gpio_pin_expression(config[CONF_STEP_PIN_2])
    cg.add(var.set_step_pin_2(step_pin_2))
    dir_pin = await cg.gpio_pin_expression(config[CONF_DIR_PIN])
    cg.add(var.set_dir_pin(dir_pin))

    if CONF_SLEEP_PIN in config:
        sleep_pin = await cg.gpio_pin_expression(config[CONF_SLEEP_PIN])
        cg.add(var.set_sleep_pin(sleep_pin))
