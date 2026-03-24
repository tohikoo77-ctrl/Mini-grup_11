from django.db import models
from django.utils.translation import gettext_lazy as _
from icecream import ic


class DiscountTypes(models.TextChoices):
    PERCENT = "percent", _("Percent")
    AMOUNT = "amount", _("Amount")

    def __str__(self):
        return str(self.label)


class NotificationStates(models.TextChoices):
    NEW = "new", _("New")
    READ = "read", _("Read")

    def __str__(self):
        return str(self.label)


class UserRoles(models.TextChoices):
    ORDINARY_USER = "ordinary_user", _("Ordinary User")
    CUSTOMER = "customer", _("Customer")
    BARBER = "barber", _("Barber")
    MANAGER = "manager", _("Manager")
    ADMIN = "admin", _("Admin")
    SUPER_ADMIN = "super_admin", _("Super Admin")

    def __str__(self):
        return str(self.label)


class Genders(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")

    def __str__(self):
        return str(self.label)


class AuthStatuses(models.TextChoices):
    NEW = "new", _("New")
    CODE_VERIFIED = "code_verified", _("Code Verified")
    DONE = "done", _("Done")

    def __str__(self):
        return str(self.label)


class AuthTypes(models.TextChoices):
    VIA_PHONE = "via_phone", _("Via Phone")
    VIA_EMAIL = "via_email", _("Via Email")

    def __str__(self):
        ic(str(self.label), self.VIA_EMAIL, self.VIA_PHONE)
        return str(self.label)


class Themes(models.TextChoices):
    SYSTEM = "system", _("System")
    LIGHT = "light", _("Light")
    DARK = "dark", _("Dark")

    def __str__(self):
        return str(self.label)


class PaymentStatuses(models.TextChoices):
    PENDING = "pending", _("Pending")
    PAID = "paid", _("Paid")
    FAILED = "failed", _("Failed")
    REFUNDED = "refunded", _("Refunded")

    def __str__(self):
        return str(self.label)


class AppointmentStatuses(models.TextChoices):
    PENDING = "pending", _("Pending")
    SCHEDULED = "scheduled", _("Scheduled")
    CANCELED = "canceled", _("Canceled")
    RESCHEDULED = "rescheduled", _("Rescheduled")
    APPROVED = "approved", _("Approved")
    ONGOING = "ongoing", _("Ongoing")
    COMPLETED = "completed", _("Completed")
    REFUNDED = "refunded", _("Refunded")

    def __str__(self):
        return str(self.label)


class ReasonTypes(models.TextChoices):
    CHANGE_IN_PLANS = "change_in_plans", _("Change in Plans")
    UNABLE_TO_CONTACT_BARBER = "unable_to_contact_barber", _("Unable to Contact Barber")
    WRONG_ADDRESS_SHOWN = "wrong_address_shown", _("Wrong Address Shown")
    THIS_PRICE_IS_NOT_REASONABLE = "this_price_is_not_reasonable", _("This Price is Not Reasonable")
    BOOKING_MISTAKE = "booking_mistake", _("Booking Mistake")
    POOR_WEATHER_CONDITIONS = "poor_weather_conditions", _("Poor Weather Conditions")
    OTHER = "other", _("Other")

    def __str__(self):
        return str(self.label)


class SeatCount(models.TextChoices):
    ONE_SEAT = "one_seat", _("One Seat")
    TWO_SEATS = "two_seats", _("Two Seats")
    MULTIPLE = "multiple", _("Multiple Seats")

    def __str__(self):
        return str(self.label)
