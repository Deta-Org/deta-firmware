/*
 * This file is part of the detahard project, https://detahard.io/

 */

#ifndef __STORAGE_H__
#define __STORAGE_H__

#include <stddef.h>
#include <stdint.h>
#include "secbool.h"

// The length of the external salt in bytes.
#define EXTERNAL_SALT_SIZE 32

// If the top bit of APP is set, then the value is not encrypted.
#define FLAG_PUBLIC 0x80

// If the top two bits of APP are set, then the value is not encrypted and it
// can be written even when the storage is locked.
#define FLAGS_WRITE 0xC0

// The maximum value of app_id which is the six least significant bits of APP.
#define MAX_APPID 0x3F

// The PIN value corresponding to an empty PIN.
extern const uint8_t *PIN_EMPTY;
#define PIN_EMPTY_LEN 0

typedef secbool (*PIN_UI_WAIT_CALLBACK)(uint32_t wait, uint32_t progress,
                                        const char *message);

void storage_init(PIN_UI_WAIT_CALLBACK callback, const uint8_t *salt,
                  const uint16_t salt_len);
void storage_wipe(void);
secbool storage_is_unlocked(void);
void storage_lock(void);
secbool storage_unlock(const uint8_t *pin, size_t pin_len,
                       const uint8_t *ext_salt);
secbool storage_has_pin(void);
secbool storage_pin_fails_increase(void);
uint32_t storage_get_pin_rem(void);
secbool storage_change_pin(const uint8_t *oldpin, size_t oldpin_len,
                           const uint8_t *newpin, size_t newpin_len,
                           const uint8_t *old_ext_salt,
                           const uint8_t *new_ext_salt);
void storage_ensure_not_wipe_code(const uint8_t *pin, size_t pin_len);
secbool storage_has_wipe_code(void);
secbool storage_change_wipe_code(const uint8_t *pin, size_t pin_len,
                                 const uint8_t *ext_salt,
                                 const uint8_t *wipe_code,
                                 size_t wipe_code_len);
secbool storage_has(const uint16_t key);
secbool storage_get(const uint16_t key, void *val, const uint16_t max_len,
                    uint16_t *len);
secbool storage_set(const uint16_t key, const void *val, const uint16_t len);
secbool storage_delete(const uint16_t key);
secbool storage_set_counter(const uint16_t key, const uint32_t count);
secbool storage_next_counter(const uint16_t key, uint32_t *count);

#endif
