/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 17:22:13 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/11 17:22:14 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

char *ft_itoa_base_up(unsigned long num, int base)
{
    static char digits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char buffer[65];
    int i = 0;
    int negative = 0;

    if (base < 2 || base > 36)
        return NULL;
    if (num == 0)
    {
        buffer[i++] = '0';
    }
    else
    {
        if (num < 0 && base == 10)
        {
            negative = 1;
            num = -num;
        }

        while (num > 0)
        {
            buffer[i++] = digits[num % base];
            num /= base;
        }

        if (negative)
            buffer[i++] = '-';
    }
    buffer[i] = '\0';
    char *result = malloc(i + 1);
    if (!result)
        return NULL;
    int j = 0;
    while (i > 0)
        result[j++] = buffer[--i];
    result[j] = '\0';
    return result;
}

char *ft_itoa_base_low(unsigned long num, int base)
{
    static char digits[] = "0123456789abcdefghijklmnopqrstuvwxyz";
    char buffer[65];
    int i = 0;
    int negative = 0;

    if (base < 2 || base > 36)
        return NULL;

    if (num == 0)
    {
        buffer[i++] = '0';
    }
    else
    {
        if (num < 0 && base == 10)
        {
            negative = 1;
            num = -num;
        }

        while (num > 0)
        {
            buffer[i++] = digits[num % base];
            num /= base;
        }

        if (negative)
            buffer[i++] = '-';
    }

    buffer[i] = '\0';

    char *result = malloc(i + 1);
    if (!result)
        return NULL;

    int j = 0;
    while (i > 0)
        result[j++] = buffer[--i];

    result[j] = '\0';

    return result;
}
