class TeslaVehicle(object):
    def __init__(self, id, api):
        self.id = id
        self.api = api
        self.api.prefix_url = self.api.prefix_url + '/api/1/vehicles/%s' % self.id

    def get_vehicle_data(self):
        url = '/vehicle_data'
        return self.api.get(url).json()['response']

    def wake_up(self):
        url = '/wake_up'
        return self.api.post(url).json()['response']

    def honk_horn(self):
        url = '/command/honk_horn'
        return self.api.post(url).json()['response']

    def flash_lights(self):
        url = '/command/flash_lights'
        return self.api.post(url).json()['response']

    def remote_start_drive(self):
        url = '/command/remote_start_drive'
        raise NotImplementedError

    def speed_limit_set_limit(self, limit):
        """
        input
        limit: (int) speed limit in mph, must be between 50 and 90
        """
        raise NotImplementedError

    def speed_limit_activate(self, pin):
        """
        input
        pin: (str) existing pin if previously set or a new pin
        """
        raise NotImplementedError

    def speed_limit_deactivate(self, pin):
        """
        input
        pin: (str) pin to deactivate speed limit
        """
        raise NotImplementedError

    def speed_limit_clear_pin(self, pin):
        """
        input
        pin: (str) pin used when activating speed limit
        """
        raise NotImplementedError

    def set_valet_mode(self, state, pin):
        """
        input
        state: (bool) true to activate, false to deactivate
        pin: (str) pin to deactivate valet mode
        """
        raise NotImplementedError

    def reset_valet_pin(self):
        raise NotImplementedError

    def door_unlock(self):
        raise NotImplementedError

    def door_lock(self):
        raise NotImplementedError

    def actuate_trunk(self, position):
        """
        input:
        position: (str) either `front` or `rear`
        """
        raise NotImplementedError

    def sun_roof_control(self, state):
        """
        input:
        state: (str) either `vent` or `close`
        """
        raise NotImplementedError

    def charge_port_door_open(self):
        raise NotImplementedError

    def charge_port_door_close(self):
        raise NotImplementedError

    def charge_start(self):
        raise NotImplementedError

    def charge_stop(self):
        raise NotImplementedError

    def charge_standard(self):
        raise NotImplementedError

    def charge_max_range(self):
        raise NotImplementedError

    def set_charge_limit(self, percent):
        """
        input
        percent: (int) ther percentage the battery will be
        charged until must be between 10 and 100
        """
        raise NotImplementedError

    def auto_conditioning_start(self):
        raise NotImplementedError

    def auto_conditioning_stop(self):
        raise NotImplementedError

    def set_temps(self, driver_temp, passenger_temp):
        """
        input
        driver_temp: (long) desired temp on driver's side in celsius
        passenger_temp: (long) desired temp on driver's side in celsius
        """
        raise NotImplementedError

    def remote_seat_heater_request(self, heater, level):
        """
        input
        heater: (int) desired seat to heat (0-4)
        level: (int) desired level for heater (0-3)
        """
        raise NotImplementedError

    def media_toggle_playback(self):
        raise NotImplementedError

    def media_next_track(self):
        raise NotImplementedError

    def media_prev_track(self):
        raise NotImplementedError

    def media_next_fav(self):
        raise NotImplementedError

    def media_prev_fav(self):
        raise NotImplementedError

    def media_volume_up(self):
        raise NotImplementedError

    def media_volume_down(self):
        raise NotImplementedError

    def navigation_request(self, locale, value):
        """
        input
        locale: (str) the locale for the navigation request
        value: (str) the address to set as the destination
        """
        raise NotImplementedError

    def schedule_software_update(self, offset_sec):
        """
        input
        offset_sec: (int) number of seconds in the future
        to schedule the software update
        """
        raise NotImplementedError

    def cancel_software_update(self):
        raise NotImplementedError
