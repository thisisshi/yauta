import time
from requests.exceptions import HTTPError

from yauta.exceptions import TeslaException

METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PATCH = 'PATCH'
METHOD_DELETE = 'DELETE'


class TeslaVehicle(object):

    def __init__(self, id, api):
        self.id = id
        self.api = api
        self.api.prefix_url = self.api.prefix_url + '/api/1/vehicles/%s' % self.id # noqa

    def _call(self, method: str, url: str, data: dict) -> dict:
        """
        Make calls via http

        Since all of the methods on TeslaVehicle should raise on error,
        this is a centralized method make all the various HTTP calls from.

        input
        method: one of 'GET', 'POST'
        url: the api endpoint without the prefix url
        data: a data payload if necessary
        """

        if method == METHOD_POST:
            if data:
                resp = self.api.post(url, data=data)
            else:
                resp = self.api.post(url)
        elif method == METHOD_GET:
            resp = self.api.get(url)

        try:
            resp.raise_for_status()
        except HTTPError as e:
            raise TeslaException(
                'Unable to complete request to: %s - %s' % (url, e))

        return resp.json()['response']

    def get_vehicle_data(self) -> dict:
        """
        Get detailed vehicle data
        """

        url = '/vehicle_data'
        data = None
        return self._call(METHOD_GET, url, data)

    def wake_up(self) -> dict:
        """
        Wake up vehicle
        """

        url = '/wake_up'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def honk_horn(self) -> dict:
        """
        Honk the horn
        """

        url = '/command/honk_horn'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def flash_lights(self) -> dict:
        """
        Flash the front lights
        """

        url = '/command/flash_lights'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def remote_start_drive(self, password: str) -> dict:
        """
        Enable keyless remote driving

        input
        password (str): password for tesla account
        """

        url = '/command/remote_start_drive'
        data = {
            'password': password
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def speed_limit_set_limit(self, limit: int) -> dict:
        """
        Set maximum speed limit
        input
        limit: (int) speed limit in mph, must be between 50 and 90
        """

        url = '/command/speed_limit_set_limit'
        data = {
            'limit_mph': limit
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def speed_limit_activate(self, pin: str) -> dict:
        """
        Activate maximum speed limit

        input
        pin: (str) existing pin if previously set or a new pin
        """

        url = '/command/speed_limit_activate'
        data = {
            'pin': pin
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def speed_limit_deactivate(self, pin: str) -> dict:
        """
        Deactivate maximum speed limit
        input
        pin: (str) pin to deactivate speed limit
        """

        url = '/command/speed_limit_deactivate'
        data = {
            'pin': pin
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def speed_limit_clear_pin(self, pin: str) -> dict:
        """
        Clears the currently set PIN for speed limit mode

        input
        pin: (str) pin used when activating speed limit
        """

        url = '/command/speed_limit_clear_pin'
        data = {
            'pin': pin
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def set_valet_mode(self, state: bool, pin: str):
        """
        Activate or deactivate valet mode

        input
        state: (bool) true to activate, false to deactivate
        pin: (str) pin to deactivate valet mode
        """

        url = '/command/set_valet_mode'
        data = {
            'on': state,
            'password': pin
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def reset_valet_pin(self) -> dict:
        """
        Clears valet PIN when valet mode is deactivated
        """

        url = '/command/reset_valet_pin'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def door_unlock(self) -> dict:
        """
        Unlock all doors
        """

        url = '/command/door_unlock'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def door_lock(self) -> dict:
        """
        Lock all doors
        """

        url = '/command/door_lock'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def actuate_trunk(self, position: int) -> dict:
        """
        Open either front or rear trunk

        On vehicles with power trunks will also close trunk

        input:
        position: (str) either `front` or `rear`
        """
        try:
            assert position in ('front', 'rear')
        except AssertionError:
            raise TeslaException(
                'Invalid position: %s, must be "front" or "rear"' % position)

        url = '/command/actuate_trunk'
        data = {
            'which_trunk': position
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def sun_roof_control(self, state: str) -> dict:
        """
        Control panoramic sunroof

        input:
        state: (str) either `vent` or `close`
        """

        try:
            assert state in ('vent', 'close')
        except AssertionError:
            raise TeslaException(
                'Invalid state: %s, must be "vent" or "close"' % state)

        url = '/command/sun_roof_control'
        data = {
            'state': state
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_port_door_open(self) -> dict:
        """
        Open charge port door
        """

        url = '/command/charge_port_door_open'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_port_door_close(self) -> dict:
        """
        Close charge port door
        """

        url = '/command/charge_port_door_close'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_start(self) -> dict:
        """
        Start charging
        """

        url = '/command/charge_start'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_stop(self) -> dict:
        """
        Stop charging
        """

        url = '/command/charge_stop'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_standard(self) -> dict:
        """
        Set charge limit to "standard" or ~90%
        """

        url = '/command/charge_standard'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def charge_max_range(self) -> dict:
        """
        Set charge limit to max range or 100%
        """

        url = '/command/charge_max_range'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def set_charge_limit(self, percent: int) -> dict:
        """
        Remotely set battery charging limit

        input
        percent: (int) the percentage the battery will be
        charged until must be between 10 and 100
        """

        try:
            assert 10 < percent < 100
        except AssertionError:
            raise TeslaException(
                "percent: %s must be between 10 and 100" % percent)

        url = '/command/set_charge_limit'
        data = {
            'percent': percent
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def auto_conditioning_start(self) -> dict:
        """
        Remotely start air conditioning
        """

        url = '/command/auto_conditioning_start'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def auto_conditioning_stop(self) -> dict:
        """
        Remotely stop air conditioning
        """

        url = '/command/auto_conditioning_stop'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def set_temps(self, driver_temp: float, passenger_temp: float) -> dict:
        """
        Remotely set internal cabin temperatures

        driver_temp and passenger_temp must be set in celsius

        input
        driver_temp: (float) desired temp on driver's side in celsius
        passenger_temp: (float) desired temp on driver's side in celsius
        """

        url = '/command/set_temps'
        data = {
            'driver_temp': driver_temp,
            'passenger_temp': passenger_temp
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def remote_seat_heater_request(self, heater: int, level: int) -> dict:
        """
        Remotely start heated seats.

        heater must be in range(5), the seat numbers
        correlate to the following:

        0 - Driver
        1 - Passenger
        2 - Rear Left
        3 - Rear Center
        4 - Rear Right

        level is the level of heat, and must be in range(3)

        input
        heater: (int) desired seat to heat (0-4)
        level: (int) desired level for heater (0-3)
        """

        try:
            assert heater in range(5)
        except AssertionError:
            raise TeslaException(
                'Invalid seat selected, seat number must be in range: %s'
                % range(5)
            )
        try:
            assert level in range(4)
        except AssertionError:
            raise TeslaException(
                'Invalid level selected, level must be in range: %s'
                % range(4)
            )

        url = '/command/remote_seat_heater_request'
        data = {
            'heater': heater,
            'level': level
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def media_toggle_playback(self) -> dict:
        """
        Toggle media playback
        """

        url = '/command/media_toggle_playback'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_next_track(self) -> dict:
        """
        Play next track
        """

        url = '/command/media_next_track'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_prev_track(self) -> dict:
        """
        Play previous track
        """

        url = '/command/media_prev_track'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_next_fav(self) -> dict:
        """
        Play next favorite
        """

        url = '/command/media_next_fav'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_prev_fav(self) -> dict:
        """
        Play previous favorite
        """

        url = '/command/media_prev_fav'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_volume_up(self) -> dict:
        """
        Turn media volume up
        """

        url = '/command/media_volume_up'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def media_volume_down(self) -> dict:
        """
        Turn media volume down
        """

        url = '/command/media_volume_down'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)

    def navigation_request(self, locale: str, value: str) -> dict:
        """
        Set navigation

        input
        locale: (str) the locale for the navigation request
        value: (str) the address to set as the destination
        """
        url = '/command/navigation_request'
        timestamp = time.time()
        data = {
                'type': 'share_ext_content_raw',
                'locale': locale,
                'timestamp_ms': timestamp,
                'value[android.intent.extra.TEXT]': value
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def schedule_software_update(self, offset_sec: int) -> dict:
        """
        Schedule software update

        input
        offset_sec: (int) number of seconds in the future
        to schedule the software update
        """
        url = '/command/schedule_software_update'
        data = {
            'offset_sec': offset_sec
        }
        method = METHOD_POST
        return self._call(method, url, data)

    def cancel_software_update(self) -> dict:
        url = '/command/cancel_software_update'
        data = None
        method = METHOD_POST
        return self._call(method, url, data)
